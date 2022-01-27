#Copyright (c) 2022 Jonas Lütolf 
FULL="█"
RIGHT="▐"
LEFT="▌"
BOTTOM="▄"
TOP="▀"

class PixelGrafik:
    def __init__(self,x_len:int,y_len:int)->None:
        self.y_len=y_len
        self.x_len=x_len
        
        #Feld erstellen
        self.field=[]
        for y in range(0,self.y_len):
            temp=[]


            for x in range(0,self.x_len):
                temp.append(" ")

            self.field.append(temp)

    def set_pixel(self,x:int,y:int,icon=FULL)->bool:
        if len(icon)>1 or len(icon)<1:
            return False
        self.field[y][x]=icon
        return True

    def add_text(self,text:str,y:int,x=0)->bool:
        if len(text) > self.x_len or x+len(text) > self.x_len or "\n" in text:
            return False
        
        else:
            for i in text:
                self.field[y][x]=i
                x+=1
            return True
              
    def __str__(self)->str:
        ret=""
        for y in self.field:
            for x in y:
                ret+=x
            ret+="\n"
        return ret[0:-1]

    def get_line(self,y:int)->str:
        ret=""
        for x in self.field[y]:
                ret+=x
        return ret

    def get_pixel(self,x:int,y:int)->str:
        return self.field[y][x]
        
    def clear(self)->None:
        self.field=[]
        for y in range(0,self.y_len):
            temp=[]
            for x in range(0,self.x_len):
                temp.append(" ")

            self.field.append(temp)

class Diagram(PixelGrafik):
    def __init__(self, x_len:int, y_len:int)->None:
        super().__init__(x_len, y_len)
       
    def set_data(self, data:list)->None:
        self.clear()
        if len(data)<self.x_len:
            data+=[0]*(self.x_len-len(data))

        x=0
        for i in data:
            self.set_pixel(x,10-i//10)
            x+=1