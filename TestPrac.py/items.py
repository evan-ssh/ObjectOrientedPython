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
    
class Store:
    def __init__(self):
        self.__items = []

    def loadItems(self):
        filename = 'items.csv'
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                item = row[0]
                price = int(row[1])
                self.__items.append(Item(item,price))

    def listItems(self):
        print("Welcome to the dollar store")
        for item in self.__items:
            print(item.name)

    def sellItems(self,name,quantity):
        for item in self.__items:
            if item.name == name:
                return f"{quantity} {item.name}'s cost {item.price * quantity}" 
        else:
            return f"Sorry we do not have {name}'s"
    def main():
        store = Store()
        store.loadItems()
        while True:
            store.listItems()
            command = input("Would u like to purchase an item?")
            if command != "y":
                continue
            name = input("Enter name of item: ")
            quantity = int(input("How many would you like?: "))
            sold = store.sellItems(name,quantity)
            print(sold)
    if __name__ == "__main__":
        main()