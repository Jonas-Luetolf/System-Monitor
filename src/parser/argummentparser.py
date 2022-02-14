class ParseError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "ParseError"

class Flag:
    def __init__(self,flag:str,options:int,flag_symbol="-"):
        self.flag=flag
        self.options=options
        self.symbol=flag_symbol

    def __str__(self):
        return self.symbol*((len(self.flag)>1)+1)+self.flag

class ArgummentParser:
    def __init__(self,commands:list):
        self.commands=commands
        self.flags=[]

    def add_flag(self,flag:str,options:int):
            self.flags.append(Flag(flag,options))

    def parse(self,to_parse:list):
        x=0
        ret_command=None
        ret_flags={}
        while x<len(to_parse):
            aktuell_arg=to_parse[x]

            if aktuell_arg in self.commands and ret_command==None:
                ret_command=aktuell_arg
                x+=1

            elif aktuell_arg in (str(i) for i in self.flags):
                for flag in self.flags:
                    if str(flag)==aktuell_arg:
                        ret_flags.update({str(flag):to_parse[x+1:x+2+flag.options]})
                        x=x+2+flag.options
                        break

            else:
                print(x)
                raise ParseError
        return ret_command,ret_flags
