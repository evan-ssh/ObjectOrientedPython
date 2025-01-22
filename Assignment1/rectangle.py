class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calculate_perimter(self):
        return (self.height * 2) + (self.width * 2)
    
    def calculate_area(self):
        return self.height * self.width 