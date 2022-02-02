#Copyright (c) 2022 Jonas Lütolf 
from os import lseek
import time
import src.diagram.diagram as diagram
import src.backend as backend
import src.style.widget as widget

class frontend:
    def __init__(self,backend_handler:backend.Handler,cpu_usage_diagram:diagram.Diagram) -> None:
        self.cpu_usage_diagram=cpu_usage_diagram
        self.backend_handler=backend_handler
        self.config=self.backend_handler.get_config()

    def get_data(self,objects:list)->dict:
        return self.backend_handler.get_data(objects)

    def start_loop(self)->None:
        while True:
            aktuell_data=self.get_data(["general","cpu","ram","disks"])
            self.format_cpu_data(aktuell_data["cpu"])
            time.sleep(int(self.config["update_time"])-int(self.config["data_load_time"]))

    def print_help(self)->None:
        help_data=self.backend_handler.get_help_data()
        print(help_data)

    def print_data(self,data:dict)->None:
        pass

    def format_cpu_data(self,data):
        self.cpu_usage_diagram.set_data(data['general_usage'])
        ret=widget.Widget("CPU")
        ret[0]=f"Frequenz: {data['max_freq']}"
        ret[1]=f"Cores: {data['num_cores']}"
        ret[2]=f"Usage: {data['general_usage']}%{self.cpu_usage_diagram}"
        print(ret)
        
