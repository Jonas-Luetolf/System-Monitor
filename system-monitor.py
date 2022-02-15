from src.backend import Handler
from src.frontend import Frontend
from src.diagram.diagram import Diagram
from src.parser.argummentparser import ArgummentParser
from sys import argv
from os.path import expanduser

def main()->None: 
    #argumment parsing
    arg_parser=ArgummentParser(["loop","setconf"])
    arg_parser.add_flag("file",1)
    arg_parser.add_flag("config",1)
    try:
        command,flags=arg_parser.parse(argv[1:])
    except ParseError:
        print("Unknown command or flag")
    #find config path
    if "--config" in flags:
        config_path=flags["--config"][0]

    else:
        config_path=f"{expanduser('~')}/.config/System-Monitor/config.yaml"
    
    #init frontend & backend
    backend_handler=Handler(config_path)
    cpu_usage_diagram=Diagram()
    frontend=Frontend(backend_handler,cpu_usage_diagram)

    #only python3.10 and higher can execute the code
    match command:
        case "loop":
            frontend.start_loop()

        case "setconf":
            if "--file" in flags:
                backend_handler.set_config_by_file(flags["--file"][0]) 
            else:
                print("flag --file required")

        case _:
            print("no command")

if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print("\nstop program")
