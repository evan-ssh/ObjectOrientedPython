class Circle:
    def __init__(self,radius):#access modifiers like private public and protected are not in python so we use a convention with a leading underscore before any attributes we want private
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
    @property
    def diameter(self):
        return self.__radius * 2
            
c = Circle(5)
print(c.radius)#calls radius method and returns whats inside circle is not needed
print(c.diameter)
c.radius = -1
print(c.radius)
print(c.diameter)