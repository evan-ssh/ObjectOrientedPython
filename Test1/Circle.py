import math
class Circle:
    def __init__(self, radius:float, color:str):
        self.__radius = radius
        self.__color = color
    
    @property
    def radius(self):
        return self.__radius
    @property
    def color(self):
        return self.__color
    
    @radius.setter
    def radius(self,newVal):
        self.__radius = newVal
    
    @color.setter
    def color(self,newVal):
        self.__color = newVal

    def getArea(self):
        return math.pi * self.__radius * self.__radius