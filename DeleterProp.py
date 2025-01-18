class Circle:
    def __init__(self,radius):#access modifiers like private publci and protected are not in python so we use a convention with a leading underscore before any attributes we want private
        self.__radius = radius

    @property#used in combination with private attribute so that we can control the access of the attribute and wheter you can set it delete it etc
    def radius(self):#property is a getter 
        #get the radius of the circle.
        return self.__radius
    
    @radius.setter
    def radius(self,value):
        if value >= 0:
          self.__radius = value
        else:
            raise ValueError("Must be positive")
    
    @radius.deleter
    def radius(self):
        del self.__radius
        print("Deleted")       
c = Circle(5)
del c.radius