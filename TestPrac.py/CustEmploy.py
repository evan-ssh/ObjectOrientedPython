class Person:
    def __init__(self,firstName,lastName,email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def __str__(self):
        return f"{self.firstName} - {self.lastName}"
    

class Customer(Person):
    def __init__(self,firstName,lastName,email,customerNumber):
        Person().__init__(firstName,lastName,email)
        self.customerNumber = customerNumber

class Employee(Person):
    def __init__(self,firstName,lastName,email,ssn):
        Employee().__init__(firstName,lastName,email)
        self.ssn = ssn

while True:
    choice = input("Customer or Employee (c/e)")
    if choice == 'c':
        firstname = input("Enter customers first name")
        lastname = input("Enter customers last name")
        email = input("Enter customers email")
        cust_num = int(input("Enter customers number"))
        customer = Customer(firstname,lastname,email,cust_num)
    elif choice == 'e':
        firstname = input("Enter employees first name")
        lastname = input("Enter employees last name")
        email = input("Enter employees email")
        ssn = int(input("Employees SSN"))
        employee = Employee(firstname,lastname,email,ssn)
    else:
        print("Enter customer or employee")

    if isinstance(customer, Person):
        print(customer)
    elif isinstance(employee,Person):
        print(employee)
    