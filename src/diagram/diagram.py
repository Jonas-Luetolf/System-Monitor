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
    def __init__(self)->None:
        super().__init__(12,1)
       
    def set_data(self, data:float)->None:
        self.clear()
        if data>=0 and data<=100:
            data=round(data/10)
            data=int(data)
            self.set_pixel(0,0,"[")
            for i in range(1,data+1):
                self.set_pixel(i,0)
                
            self.set_pixel(11,0,"]")
