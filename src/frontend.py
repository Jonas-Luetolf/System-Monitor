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
            aktuell_data=self.get_data(["cpu","ram","disks"])
            print(aktuell_data)
            time.sleep(self.config["update_time"]-DATALOADTIME)

    def print_help(self)->None:
        help_data=self.backend_handler.get_help_data()
        print(help_data)