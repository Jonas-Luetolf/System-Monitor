#Copyright (c) 2022 Jonas Lütolf 
import src.backend as backend
import src.frontend as frontend
import src.diagram.diagram as diagram
import sys


def main(option:str)->None: 
    backend_handler=backend.Handler("config/config.yaml","config/backupconfig.yaml")
    cpu_usage_diagram=diagram.Diagram(10,10)
    Frontend=frontend.frontend(backend_handler,cpu_usage_diagram)

    if option=="--loop":
        Frontend.start_loop()

    elif option=="-h":
        Frontend.print_help()
   
        
    
    

    

if __name__ == '__main__':

    if len(sys.argv)!=2:
        main("-h")
        
    elif sys.argv[1] not in ["-loop",-"h"]:
        print("invalid argument")

    else:
        main(sys.argv[1])