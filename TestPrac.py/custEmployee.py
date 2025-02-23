class Person:
    def __init__(self,firstName,lastName,email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
    def __str__(self):
        return f"FirstName:{self.firstName} LastName:{self}."
        
class Customer(Person):
    def __init__(self,firstName,lastName,email,cust_id):
        super().__init__(firstName,lastName,email)
    
    def __str__(self):
        super().__str__() + f"Customer ID: {self.cust_id}"