import csv
class Item:
    def __init__(self,name,price):
        self.__name = name
        self.__price = price
    def __str__(self):
        return f"{self.__name} {self.__price}"
    
    @property 
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price