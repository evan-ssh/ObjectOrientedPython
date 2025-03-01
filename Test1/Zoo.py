class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def canFeed(self):
        return True

    def __str__(self):
        return "Can Feed:" + " " + str(self.canFeed()) + ", " + "Noise:" + " " + self.makeNoise() + " " + "String representation:" + " " + self.name + ", " "Age:"+ " " + self.age
    
class Donkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def makeNoise(self):
        return "hee-haw"
    
class Goat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def makeNoise(self):
        return "maaaa"

class HoneyBadger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def canFeed(self):
        return False
    
    def makeNoise(self):
        return "rattle-grunt"
    