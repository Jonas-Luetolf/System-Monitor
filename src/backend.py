import yaml

class SettingsHandler:
    def __init__(self,config_path):
        self.config_path=config_path

    def get_settings(self)->dict:
        with open(self.config_path,"r") as f:
            return yaml.load(f.read(),Loader=yaml.FullLoader)

    def set_settings(self,data:dict)->None:
        if self.valid_settings(data):
            with open(self.config_path,"w") as f:
                f.write(yaml.dump(data))
                
    def valid_settings(self,data:dict)->bool:
        return False

class Handler:
    def __init__(self,config_path:str):
        self.settings_handler=SettingsHandler(config_path)
        
    def get_config(self):
        return self.settings_handler.get_settings()

    def set_config(self,data:dict):
        self.settings_handler.set_settings(data)

    def get_data(self)->dict:
        return {}

    def get_help_data(self)->str:
        help_text_path=self.settings_handler.get_settings()["help_text_path"]
        with open(help_text_path,"r") as f:
            return f.read()




        








import os
import sys
import json
import time
import platform
import socket
import psutil
import GPUtil
def get_general_data():
    host_name=socket.gethostname()
    aktuell_time=time.asctime(time.localtime())
    os=platform.platform()
    
    return json.loads(json.dumps({"time":aktuell_time,"host_name":host_name,"os":os}))

def get_cpu_data():
    general_freq=psutil.cpu_freq(percpu=False).current
    anz_cpus=psutil.cpu_count(logical=True)
    general_usage=psutil.cpu_percent(percpu=False,interval=1)
    usage_percpu=psutil.cpu_percent(percpu=True,interval=1)
    return json.loads(json.dumps({"general_freq":general_freq,"anz_cpus":anz_cpus,"general_usage":general_usage,"usage_percpu":usage_percpu}))

def get_ram_data():
    virtual_memory=psutil.virtual_memory()
    ram_total=virtual_memory.total
    ram_used=virtual_memory.used
    ram_available=virtual_memory.available
    ram_usage=virtual_memory.percent
    return json.loads(json.dumps({"ram_total":ram_total,"ram_used":ram_used,"ram_availabe":ram_available,"ram_usage":ram_usage}))

def get_disk_data():
    disks={}
    raw_disks_infos=psutil.disk_partitions(all=False)
    for disk in raw_disks_infos:
        usage=psutil.disk_usage(disk.mountpoint)
        disks.update({disk.device:[disk.mountpoint,disk.fstype,[usage.total,usage.free,usage.used]]})

    return json.loads(json.dumps(disks))