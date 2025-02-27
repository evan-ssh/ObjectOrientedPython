import math
class Circle:
    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color
    
    @property
    def radius(self):
        return self.__radius
    @property
    def color(self):
        return self.__color
    
    @radius.setter
    def setradius(self,newVal):
        self.__radius = newVal
    
    @color.setter
    def setcolor(self,newVal):
        self.__color = newVal