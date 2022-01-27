import sys
class ArgumentParser:
    def __init__(self)->None:
        self.options=[]
        
    def add_option(self,flag:str,num_arguments=0)->None:
        self.options.append(Option(flag,num_arguments))

    def parse(self)->None:
        self.parsed=[]
        index=1
        while index<len(sys.argv):
            for option in self.options:
                if sys.argv[index]==option.flag:
                    end_index=index+option.num_arguments+1
                    self.parsed.append(sys.argv[index:end_index])
                    index=end_index
                    break
                
    def __getitem__(self,item:(str or int))->list:
        if type(item)==int:
            return self.parsed[item]

        else:
            for i in self.parsed:
                
                if i[0] == item:
                    return i
            raise IndexError
      
class Option:
    def __init__(self,flag:str,num_arguments=0)->None:
        self.flag=flag
        self.num_arguments=num_arguments


