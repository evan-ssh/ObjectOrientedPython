from dataclasses import dataclass

@dataclass#reads through the different attributes with their type annotation str,flt,int and automatically populate the init,wrapper,equal method for us plus more
class Product:
    name: str
    price: float
    quantity : int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity
    
#With the dataclass we dont need to write the init, wrapper, or equal method they are automatically implemented for us

p1 = Product(name="Laptop", price=1000, quantity=4)

p2 = Product(name="XBOX", price=1000, quantity=3)
p3 = Product(name="PlayStation", price=1000, quantity=2)
p4 = Product(name="Laptop", price=1000, quantity=4)

print(p1)# prints name="Laptop", price=1000, quantity=4
print(p1.total_cost())
print(p1 == p2)# returns false
print(p1 == p3)#returns false
print(p1 == p4)#returns true