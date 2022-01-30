#Copyright (c) 2022 Jonas Lütolf 
import time
import src.diagram.diagram as diagram
import src.backend as backend
DATALOADTIME=2
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

            aktuell_data=self.get_data(["frontend","cpu","ram","disks"])

            self.print_data(aktuell_data)
            time.sleep(self.config["update_time"]-DATALOADTIME)

    def print_help(self)->None:
        help_data=self.backend_handler.get_help_data()
        print(help_data)

    def print_data(self,data:dict)->str:
        print(self.format_cpu_data(self.format_cpu_data(data["cpu"])))

    def format_cpu_data(self,cpu_data:dict)->str:
        usage_per_cpu=""
        for index,item in enumerate(cpu_data['usage_percpu']):
            usage_per_cpu+=f"[index:item]"
        self.cpu_usage_diagram.set_data(cpu_data['general_usage'])      
        ret = f"CPU:\nCores: {cpu_data['num_cores']}\nMax frequence: {cpu_data['max_freq']}\nGenaral usage: {cpu_data['general_usage']}\nUsage per cpu: {usage_per_cpu}\nGeneral Usage: {str(self.cpu_usage_diagram)}"
        return ret