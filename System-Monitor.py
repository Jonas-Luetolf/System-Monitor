import src.backend as backend
import src.frontend as frontend
import src.diagram.diagram as diagram
import src.parser.parser as parser
import sys
from os.path import *

def main()->None: 
    argparser=parser.ArgumentParser()
    argparser.add_option("--loop")
    argparser.add_option("--setconf",1)
    argparser.parse()

    backend_handler=backend.Handler(f"{expanduser('~')}/.config/System-Monitor/config.yaml",f"{expanduser('~')}/.config/System-Monitor//backupconfig.yaml")
    cpu_usage_diagram=diagram.Diagram()
    Frontend=frontend.frontend(backend_handler,cpu_usage_diagram)

#only python3.10 and higher can execute the code
    match argparser[0][0]:
        case "--loop":
            Frontend.start_loop()

        case "--setconf":
            backend_handler.set_config_by_file(argparser[0][1]) 

   
if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(exc)
