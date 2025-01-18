class Person:
    number_of_people = 0#class attribute because it does not use self
    def __init__(self,name):#instace attribute because it uses self
        self.name = name
        Person.add_person()
    @classmethod#Act on the class itself do not have access to any instance
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
p1 = Person("tim")
p2 = Person("jiill")
print(Person.number_of_people_())#acceses number_of_people because it is a class method that only accesses the class attributes or anything specifc to the class