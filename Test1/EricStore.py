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
    
class ShoppingCart:
    def __init__(self):
        self.__cart = []
    
    def addItem(self,item):
        self.__cart.append(item)
    
    def removeItem(self,productName):
        for item in self.__cart:
            if item.name == productName:
                self.__cart.remove(item)
                return f"{productName} was removed from your cart"
            else:
                return f"{productName} was not found in your cart"
            
    def amountCart(self):
        return len(self.__cart)
    
    def calculateTotal(self):
        total = 0
        for item in self.__cart:
            total += item.price * item.quantity
        return total
def displayMenu():
    print("1. Add Item to Cart")
    print("2. Remove an item")
    print("3. Check out")

def main():
    displayMenu()
    store = ShoppingCart()
    while True:
        command = int(input("Enter a command 1-3"))
        if command == 1:
            productName = input("Enter the product name")
            quantity = int(input("Enter the Product Quantity"))
            price = int(input("Enter the product price"))
            item = Item(productName,quantity,price)
            store.addItem(item)
        elif command == 2:
            if store.amountCart() == 0:
                print("Cannot remove from empty cart")
            else:
                productname = input("Enter the name of the product to remove")
                productRemoved = store.removeItem(productname)
                print(productRemoved)
        elif command == 3:
            if store.amountCart() == 0:
                print("Add some items to your cart")
            else:
                print(f"You have purchased ${store.calculateTotal()} in items")

if __name__ == "__main__":
   main()
