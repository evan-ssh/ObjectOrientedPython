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
    
    