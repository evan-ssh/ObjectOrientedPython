#Object Oriented Programming in Python

#x = 1 #X is equal to the object which is the type int equal to one
#Function are of class function whenver you create something in python you are creating an object which is an instance of a type of class

#x = 1
#y = "hello"
#print(x + y)#: unsupported operand type(s) for +: 'int' and 'str' the addition operator is not defined for int and str to be added together

#string = "hello"
#print(string.upper())#Upper is a method .operator is usually a method acting on a specific object the method upper is acting on the object string

class Dog:# created a class called dog this is a bluprint for the methods belong to the classs dog 
    def __init__(self,name,age):#this is a special method which allows us to instantiate the object when it created this methid will be ran whenever we create another object of dog it will pass any arguments called
        self.name = name #To create a dog object we need a name this is an attribute of the class dog which is name
        self.age = age
    def get_name(self):#if self is not used it will raise a type error as it needs a age
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
    def bark(self):# aa method is any function defined inside the class
        print("BARK")
    def add_one(self,x):
        return x+1






#d = Dog("Tim",34)
#d.set_age(32)#calls the method of set age on the dog object
#print(d.get_age())#returns the age we just set


#d = Dog()#variable d is assigned to a instance of the class dog
#print(d)#<__main__.Dog object at 0x00000253BCD7EC50> this i stelling us what module in memory the object of class dog was ran
#d.bark()#you can call the method on d object which prints because it is part of the dog class
#print(d.add_one(5))#we can make methods with different arguements or parameters which means u need to pass in specific values so the method can work 
#print(type(d))
#d = Dog("tim",5)#every time one of these functions is called we will pass a reference to dog
#print(d.get_name())
#print(d.get_age())
#d2 = Dog("bill",43) # we created two objects one named tim one named bill both store different names in there instance

#
