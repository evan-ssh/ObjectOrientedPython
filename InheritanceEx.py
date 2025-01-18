class Pet:#parent
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont know what i say")    
class Cat(Pet):#inheriting the upper level class pet
    def __init__(self, name, age,color):
        super().__init__(name,age)#super references the class we have inherited from
        self.color = color

    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and i am {self.color}")

class Dog(Pet):#child classes if a method in the child class is the same as the parent it will use he parents class
    def speak(self):
        print("Bark")

class Fish(Pet):#because speak wasn't defined here it can still use the parents class method
    pass


p = Pet("Tim",19)
p.speak()
c = Cat("Bill",34,"Black")
c.speak()
c.show()
d = Dog("Jill",25)
d.speak()
f = Fish("Bubbles",10)
f.speak