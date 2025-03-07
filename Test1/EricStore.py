class Item:
    def __init__(self,name,quantity,price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property
    def name(self):
        return self.__name
    
    @property
    def quantity(self):
        return self.__quantity
    
    @property
    def price(self):
        return self.__price
    
    def __str__(self):
        return f"Name: {self.__name} Quantity: {self.__quantity} Price: {self.__price}"