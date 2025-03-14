class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return (self.height * 2) + (self.width * 2)
    
    def calculate_area(self):
        return self.height * self.width 
    
    def display_rectangle(self):
        for row in range(self.height):
            if row == 0 or row == self.height - 1:
                print('*' * self.width)
            else:
                print('*' + (' ' * (self.width-2)) + '*')

if __name__ == "__main__":
    height = int(input("Height: "))
    width = int(input("Width:"))
    r = Rectangle(height,width)
    print(f"Perimeter:{r.calculate_perimeter()}")
    print(f"Area:{r.calculate_area()}")
    r.display_rectangle()