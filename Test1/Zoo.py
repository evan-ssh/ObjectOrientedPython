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

def main():
    a1 = Donkey("Donkey1","7")
    a2 = Donkey("Donkey2","3")
    a3 = Goat("Goat1","2")
    a4 = Goat("Goat2","1")
    a5 = HoneyBadger("HoneyBadger1","4")
    a6 = HoneyBadger("HoneyBader2","8")


    zoo = Zoo()
    zoo.addAnimal(a1)
    zoo.addAnimal(a2)
    zoo.addAnimal(a3)
    zoo.addAnimal(a4)
    zoo.addAnimal(a5)
    zoo.addAnimal(a6)

    count = 0
    for animal in zoo:
        count += 1
        print(animal)
    print(f"{zoo}, {count} animals")
if __name__ == "__main__":
    main()

