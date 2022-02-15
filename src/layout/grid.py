class Grid:
    def __init__(self)->None:
        self.lines=[]
    
    def clear(self)->None:
        self.lines=[]

    def add_widget(self,widget,y:int)->None:
        if y>=len(self.lines):
            self.lines+=(Line() for i in range(0,y+1-len(self.lines)))

        self.lines[y].add_widget(widget)

    def __str__(self)->str:
        return "".join(list(str(i) for i in self.lines))

class Line:
    def __init__(self)->None:
        self.widgets=[]

    def add_widget(self,widget)->None:
        self.widgets.append(widget)
    
    def clear(self)->None:
        self.widgets=[]
    
    def __str__(self)->str:
        x_lens=list(i.get_x_len()+2 for i in self.widgets)
        lines=[]
        anz_widgets=0
        for i in self.widgets:      
            for index,line in enumerate(i):
                tabs=""                
                if index>=len(lines):
                    lines+=(list([] for i in range(0,index+1-len(lines))))
                    tabs="".join(list(" "*i for i in x_lens[0:anz_widgets]))
                
                lines[index]+=tabs+line

            anz_widgets+=1

        ret=""
        for line in lines:
            ret+="".join(line)
            ret+="\n"

        return ret
