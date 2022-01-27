class ArgumentParser:
    def __init__(self)->None:
        pass

    def add_argument(self)->None:
        pass

    def parse(self):
        pass

    def print_help(self):
        pass


class Argument:
    def __init__(self,flag,function,help_text="",num_arguments=0):
        self.flag = flag
        self.function=function
        self.help_text=self.flag+": "+help_text
        self.num_arguments=num_arguments

    def call_function(self):
        self.function()






