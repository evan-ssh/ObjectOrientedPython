import math
class Circle:
    def __init__(self,radius:float,color:str):
        self.__radius = radius
        self.__color = color

    @property
    def radius(self):
        return self.__radius
    @property
    def color(self):
        return self.__color
    
    @radius.setter
    def radius(self,data):
        self.__radius = data
    @color.setter
    def color(self,data):
        self.__color = data
    
    def getArea(self):
        return math.pi * self.__radius * self.__radius
    
    def getCircumference(self):
        return 2 * math.pi * self.__radius
    def __str__(self):
        return f"radius: {self.__radius} color: {self.__color}"
def main():
    while True:
        radius = float(input("Enter the radius for your circle"))
        color = input("Enter the color for the circle")
        circle = Circle(radius,color)
        print(f"Area is {circle.getArea()}")
        print(f"Circumference is {circle.getCircumference()}")
        print(circle)
        go_again = input("Would u like to create another circle?")
        if go_again != "y":
            break

if __name__ == "__main__":
    main()