#Copyright (c) 2022 Jonas Lütolf 
import os
import time
import src.diagram.diagram as diagram
import src.backend as backend
from src.layout.widget import Widget
from src.layout.grid import Grid,Line



class frontend:
    def __init__(self,backend_handler:backend.Handler,cpu_usage_diagram:diagram.Diagram) -> None:
        self.cpu_usage_diagram=cpu_usage_diagram
        self.backend_handler=backend_handler
        self.config=self.backend_handler.get_config()
        self.grid=Grid()

    def clean(self):
        if os.name=="nt":
            os.system("cls")

        else:
            os.system("clear")

    def get_data(self,objects:list)->dict:
        return self.backend_handler.get_data(objects)

    def start_loop(self)->None:
        while True:
            aktuell_data=self.get_data(["general","cpu","ram","disks"])
            self.print_data(aktuell_data)
            time.sleep(int(self.config["update_time"])-int(self.config["data_load_time"]))

    def print_help(self)->None:
        help_data=self.backend_handler.get_help_data()
        print(help_data)

    def print_data(self,data:dict)->None:
        self.clean()
        self.grid.clear()
        self.grid.add_widget(self.format_cpu_data(data["cpu"]),0)
        print(self.grid)

    def format_cpu_data(self,data):
        self.cpu_usage_diagram.set_data(data['general_usage'])
        ret=Widget("CPU")
        ret[0]=f"Frequenz: {data['max_freq']}"
        ret[1]=f"Cores: {data['num_cores']}"
        ret[2]=f"Usage: {data['general_usage']}%{self.cpu_usage_diagram}"
        return ret       
