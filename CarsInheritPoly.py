from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        print(f"The {self.brand} {self.model} is starting.")    

    def __str__(self):
        return f"{self.model} is a family car"

#class to be composed
class Battery:
    def __init__(self,capacity):
        self.capacity = capacity
    def __str__(self):
        return f"{self.capacity}% battery"
#Child class
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        Car.__init__(self,brand, model, year)#Make sure parent passes self
        self.battery = Battery(battery_capacity)#example of composition

    def start(self):#overriding the start method ex of polymorphism
        print(f"The {self.brand} {self.model} is starting silently")

    def __str__(self):
        return f"{self.model} is an electric car has a charge of {self.battery}."

class SportsCar(Car):
    def __init__(self, brand, model, year, horsepower):
        Car.__init__(self,brand, model, year)
        self.horsepower = horsepower
    def start(self):
        print(f"The {self.brand} {self.model} is a mean machine with {self.horsepower} horses.")

    def __str__(self):
        return f"{self.model} is a sports car"
    
class Sedan(Car):
    def __init__(self,brand,model,year,color):
        Car.__init__(self,brand,model,year)
        self.color = color
    def start(self):
        print(f"The {self.color} {self.brand} {self.model} is starting with a roar.")
    def __str__(self):
        return f"{self.model} is a sporty stylish sedan"

#Create Objects

car1 = ElectricCar("Tesla","Model S",2020, 100)
car2 = SportsCar("Ferrari","F8 Tributo",2021,"710")
car3 = Sedan("Honda","Civic",2018,"Black")

#Use the str method

print(car1)
print(car2)
print(car3)

#using polymorphism

car1.start()
car2.start()
car3.start()

