class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calcPerimeter(self):
        return (self.height * 2) + (self.width * 2)
    
    def calcArea(self):
        return self.height * self.width 
    
    def __str__(self):
        strValue = ""
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1:
                    strValue += "* "
                else:
                    strValue += "  "
            strValue += "\n"
        return strValue
class Square(Rectangle):
    def __init__(self,length):
        Rectangle.__init__(self,length,length)
    

if __name__ == "__main__": 
    r = Rectangle(5,10)
    print(f"Height: {r.height}")
    print(f"Width: {r.width}")
    print(f"Perimeter: {r.calcPerimeter()}")
    print(f"Area: {r.calcArea()}")
    print(r)

    s = Square(5)
    print(f"Length: {s.height}")
    print(f"Perimeter: {s.calcPerimeter()}")
    print(f"Area: {s.calcArea()}")
    print(s)
