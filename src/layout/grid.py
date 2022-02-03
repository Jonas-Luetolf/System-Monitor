import src.layout.widget as widget
class Grid:
    def __init__(self):
        self.lines=[]
    
    def clear(self):
        del self.lines
        self.lines=[]

    def add_widget(self,widget,y):
        if y>=len(self.lines):
            for i in range(0,y+1-len(self.lines)):
                self.lines.append(Line())
        
        self.lines[y].add_widget(widget)

    def __str__(self):
        ret=""
        for i in self.lines:
            ret+=str(i)

        return ret




class Line:
    def __init__(self):
        self.widgets=[]

    def add_widget(self,widget):
        self.widgets.append(widget)
    def clear(self):
        self.widgets=[]
    def __str__(self):
        x_lens=list(i.get_x_len()+2 for i in self.widgets)
        lines=[]
        anz_widgets=0
        for i in self.widgets:
            
            for index,line in enumerate(i):
                
                try:
                    lines[index].append(line)
                
                except:
                    tabs=list(" "*i for i in x_lens[0:anz_widgets])
                    lines.append(tabs+[line])
            anz_widgets+=1

        ret=""
        for line in lines:
            for i in line:
                ret+=i
            ret+="\n"

        return ret
