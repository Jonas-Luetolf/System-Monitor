#Copyright (c) 2022 Jonas Lütolf 
import os
import yaml
import psutil
import platform
import socket
DEFAULTCONFIG="""
data_load_time: 2
update_time: 2
"""
class InvalidSettings(Exception):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "InvalidSettings: config file and backup file are invalid"

class SettingsHandler:
    def __init__(self,config_path,backup_path)->None:
        self.config_path=config_path
        self.backup_path=backup_path

    def get_settings(self)->dict:
        load_data=self.open_config(self.config_path)
        if self.valid_settings(load_data):
            pass

        elif self.valid_settings(self.open_config(self.backup_path)):
            load_data=self.open_config(self.backup_path)

        else:
            raise InvalidSettings

        return load_data

    def open_config(slef,path:str)->dict:
        try:
            with open(path,"r") as f:
                return yaml.load(f.read(),Loader=yaml.FullLoader)
        except: 
            try:
                os.mkdir(os.path.expanduser('~')+"/.config/System-Monitor/")
            except FileExistsError:
                pass
            f=open(os.path.expanduser('~')+"/.config/System-Monitor/config.yaml",'w')
            f.write(DEFAULTCONFIG)
            f.close()
            return yaml.load(DEFAULTCONFIG,Loader=yaml.FullLoader)

    def set_settings(self,data:dict)->None:
        if self.valid_settings(data):
            with open(self.config_path,"w") as f:
                f.write(yaml.dump(data))
            
            with open(self.backup_path,"w")as f:
                f.write(yaml.dump(data))
        else:
            raise InvalidSettings
                
    def valid_settings(self,data:dict)->bool:
        ret:list=[]
        #ret.append(int(os.path.isfile(data["help_text_path"])))
        ret.append(int(type(data["update_time"])==int))
        ret.append(int(type(data["data_load_time"])==int))
        if sum(ret)==len(ret):
            return True
        else:
            return False

class Handler:
    def __init__(self,config_path:str,backup_path:str)->None:
        self.settings_handler=SettingsHandler(config_path,backup_path)
        self.cpu_handler=CPU_Data_Handler()
        self.ram_handler=RAM_Data_Handler()
        self.disks_handler=Disks_Data_Handler()       
        self.get_general_data()

    def get_general_data(self)->None:
        self.os=platform.platform()
        self.hostname=socket.gethostname()

    def get_config(self)->dict:
        return self.settings_handler.get_settings()

    def set_config_by_file(self,path:str)->None:
        with open(path,"r") as f:
            data=yaml.load(f.read(), Loader=yaml.FullLoader)
        self.settings_handler.set_settings(data)

    def get_data(self,objects:list)->dict:
        ret={}
        if "general" in objects:
            ret.update({"general":{"os":self.os,"hostname":self.hostname}})

        if "cpu" in objects:
            ret.update({"cpu":self.cpu_handler.get_data()})
        
        if "ram" in objects:
            ret.update({"ram":self.ram_handler.get_data()})
            ret.update({"disks":self.disks_handler.get_data()})
        return ret
    
    def get_help_data(self)->str:
        pass

class CPU_Data_Handler:
    def __init__(self)->None:
        self.num_cores=psutil.cpu_count(logical=True)
        self.max_freq=psutil.cpu_freq(percpu=False).max

    def get_current_data(self)->dict:
        general_usage=psutil.cpu_percent(percpu=False,interval=1)
        usage_percpu=psutil.cpu_percent(percpu=True,interval=1)
        return {"general_usage":general_usage,"usage_percpu":usage_percpu}

    def get_data(self)->dict:
        ret={"num_cores":self.num_cores,"max_freq":self.max_freq}
        ret.update(self.get_current_data())
        return ret

class RAM_Data_Handler:
    def __init__(self)->None:
        self.virtual_memory=psutil.virtual_memory()
        self.total_size=self.virtual_memory.total

    def get_current_data(self)->dict:
        self.virtual_memory=psutil.virtual_memory()
        return {"used":self.virtual_memory.used,"available":self.virtual_memory.available,"usage":self.virtual_memory.percent}

    def get_data(self)->dict:
        ret={"total":self.total_size}
        ret.update(self.get_current_data())
        return ret

class Disks_Data_Handler:
    def __init__(self)->None:
        self.disks=[]
        raw_disks_data=psutil.disk_partitions(all=False)
        for disk in raw_disks_data:
            self.disks.append(Disk_Data_Handler(disk.device,disk.mountpoint,disk.fstype))

    def get_data(self)->dict:
        ret={}
        for i in self.disks:
            ret.update({i.device:i.get_data()})
        
        return ret
        
class Disk_Data_Handler:
    def __init__(self,device:str,mountpoint:str,fstype:str)->None:
        self.device=device
        self.mountpoint=mountpoint
        self.fstype=fstype
        self.total_size=psutil.disk_usage(self.mountpoint).total

    def get_current_data(self)->dict:
        usage=psutil.disk_usage(self.mountpoint)
        free=usage.free
        used=usage.used
        return {"free":free,"used":used}

    def get_data(self)->dict:
        ret={"mountpoint":self.mountpoint,"fstype":self.fstype,"totalsize":self.total_size}
        ret.update(self.get_current_data())
        return ret
