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

class Zoo:
    def __init__(self):
        self.animals = []

    def addAnimal(self,animal):
        self.animals.append(animal)


    def __str__(self):
        return f"Eric's Zoo"

    def __iter__(self):
        for animal in self.animals:
            yield animal