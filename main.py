import src.backend as backend
import src.frontend as frontend
import src.diagram.diagram as diagram
import src.parser.parser as parser
import sys


def main(option:list)->None: 
    backend_handler=backend.Handler("config/config.yaml","config/backupconfig.yaml")
    cpu_usage_diagram=diagram.Diagram(10,10)
    Frontend=frontend.frontend(backend_handler,cpu_usage_diagram)

#only python3.10 and higher can execute the code
    match option[0]:
        case "--loop":
            Frontend.start_loop()

        case "--help":
            Frontend.print_help()

   
if __name__ == '__main__':
    argparser=parser.ArgumentParser()
    argparser.add_option("--loop")
    argparser.add_option
    argparser.add_option("-help")
    argparser.parse()

    main(argparser[0])   
