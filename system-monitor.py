import src.backend as backend
import src.frontend as frontend
import src.diagram.diagram as diagram
import src.parser.argummentparser as argummentparser
import sys
from os.path import expanduser

def main()->None: 
    
    #argumment parsing
    arg_parser=argummentparser.ArgummentParser(["loop","setconf"])
    arg_parser.add_flag("file",1)
    command,flags=arg_parser.parse(sys.argv[1:])

    #init frontend & backend
    backend_handler=backend.Handler(f"{expanduser('~')}/.config/System-Monitor/config.yaml")
    cpu_usage_diagram=diagram.Diagram()
    Frontend=frontend.frontend(backend_handler,cpu_usage_diagram)

    #only python3.10 and higher can execute the code
    match command:
        case "loop":
            Frontend.start_loop()

        case "setconf":
            backend_handler.set_config_by_file(flags["--file"][0]) 

   
if __name__ == '__main__':
    main()
