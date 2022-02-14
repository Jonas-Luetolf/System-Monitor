#Copyright (c) 2022 Jonas Lütolf 
from os import system,name
from time import sleep
from src.layout.widget import Widget
from src.layout.grid import Grid, Line


def change_suffix(num,base=1024,typ="B",types=["","K","M","G","T","P","E"]):
    for i in types:
        if num>base:
            num/=base
        else:
            return f"{round(num,2)}{i}{typ}"
    return f"{round(num,2)}{types[-1]}{typ}"

class Frontend:
    def __init__(self,backend_handler,cpu_usage_diagram) -> None:
        self.cpu_usage_diagram=cpu_usage_diagram
        self.backend_handler=backend_handler
        self.config=self.backend_handler.get_config()
        self.grid=Grid()
    
    @staticmethod
    def clean()->None:
        if name=="nt":
            system("cls")

        else:
            system("clear")

    def get_data(self,objects:list)->dict:
        return self.backend_handler.get_data(objects)

    def start_loop(self)->None:
        while True:
            aktuell_data=self.get_data(self.config["loop_objects"])
            self.print_data(aktuell_data,self.config["loop_objects"])
            sleep(int(self.config["update_time"])-int(self.config["data_load_time"]))

    def print_help(self)->None:
        help_data=self.backend_handler.get_help_data()
        print(help_data)

    def print_data(self,data:dict,objects)->None:
        self.clean()
        self.grid.clear()
        y=0
        if "general" in objects:
            self.grid.add_widget(self.format_general_data(data["general"]), y)
            y+=2

        if "cpu" in objects:
            self.grid.add_widget(self.format_cpu_data(data["cpu"]),y//2)
            y+=1 
        if "ram" in objects:
            self.grid.add_widget(self.format_ram_data(data["ram"]),y//2)
            y+=1 
        if "disks" in objects:
            for disk in self.format_disk_data(data["disks"]):
                self.grid.add_widget(disk,(y)//2)
                y+=1
        print(self.grid)
    
    @staticmethod
    def format_general_data(data):
        ret=Widget("GeneralData")
        ret[0]=f"OS: {data['os']}"
        ret[1]=f"Hostname: {data['hostname']}"
        return ret

    def format_cpu_data(self,data):
        self.cpu_usage_diagram.set_data(data['general_usage'])
        ret=Widget("CPU")
        ret[0]=f"Frequenz: {data['max_freq']}"
        ret[1]=f"Cores: {data['num_cores']}"
        ret[2]=f"Usage: {data['general_usage']}%{self.cpu_usage_diagram}"
        for index,item in enumerate(data["usage_percpu"]):
            ret[3+index]=f"Usage Core{index+1}: {item}%"
        
        return ret
    
    @staticmethod
    def format_ram_data(data):
        ret=Widget("RAM")
        ret[0]=f"Total Size: {change_suffix(int(data['total']))}"
        ret[1]=f"Used Space: {change_suffix(int(data['used']))}"
        ret[2]=f"Free Space: {change_suffix(int(data['available']))}"
        return ret

    @staticmethod
    def format_disk_data(data):
        ret=[]
        for i in data:
            temp=Widget(i)
            temp[0]=f"Filesystem: {data[i]['fstype']}"
            temp[1]=f"Total Size: {change_suffix(data[i]['totalsize'])}"
            temp[2]=f"Used Space: {change_suffix(data[i]['used'])}"
            temp[3]=f"Free Space: {change_suffix(data[i]['free'])}"
            ret.append(temp)

        return ret
