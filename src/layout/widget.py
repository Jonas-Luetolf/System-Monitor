import math
class Edge:
    def __init__(self,style=2):
        self.LEFTTOP="╔"
        self.RIGHTTOP="╗"
        self.LEFTBOTTOM="╚"
        self.RIGHTBOTTOM="╝"
        self.BOTTOMTOP="═"
        self.LEFTRIGHT="║"


class Widget:
    def __init__(self,name):
        self.name = name
        self.lines=[]
        self.edge=Edge()

    def clear(self):
        self.lines=[]
    
    def __iter__(self):
        string=str(self)
        ret_list=string.split("\n")
        for i in ret_list:
            yield i

    def __setitem__(self,index,string):
        try:
            self.lines[index]=string

        except IndexError:
            for i in range(0,index+2-len(self.lines)-1):
                self.lines.append("")
            self.lines[index]=string

    def get_x_len(self):
        x_len=0
        return max(len(i) for i in self.lines+[self.name])

    def __str__(self):
        x_len=self.get_x_len()

        ret=f"{self.edge.LEFTTOP}{self.edge.BOTTOMTOP*math.ceil((x_len-1-len(self.name))/2)}{self.name}{self.edge.BOTTOMTOP*(math.ceil((x_len-len(self.name))/2))}{self.edge.RIGHTTOP}\n"
        for i in self.lines:
            ret+=f"{self.edge.LEFTRIGHT}{i}{' '*(x_len-len(i))}{self.edge.LEFTRIGHT}\n"

        return ret+self.edge.LEFTBOTTOM+self.edge.BOTTOMTOP*(x_len)+self.edge.RIGHTBOTTOM
