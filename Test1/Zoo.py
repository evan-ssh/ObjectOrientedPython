class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def canFeed(self):
        return True

    def __str__(self):
        return "Can Feed:" + " " + str(self.canFeed()) + ", " + "Noise:" + " " + self.makeNoise() + " " + "String representation:" + " " + self.name + ", " "Age:"+ " " + self.age