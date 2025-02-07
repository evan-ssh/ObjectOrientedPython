class Person():
    def __init__(Self,firstName,lastName,email):
        Self.firstName = firstName
        Self.lastName = lastName
        Self.email = email

    def __str__(self):
        return f"First Name: {self.firstName}\nLast Name: {self.lastName}\nEmail: {self.email}"
    
class Employee(Person):
    def __init__(self,firstName, lastName, email, ssn):
        Person.__init__(self,firstName,lastName,email)
        self.ssn = ssn
    
    def __str__(self):
        return f"Name: {self.firstName}\nEmail: {self.email}\nSSN: {self.ssn}"
    
class Customer(Person):
    def __init__(self, firstName, lastName, email,cust_id):
        Person.__init__(self,firstName,lastName,email)
        self.cust_id = cust_id
    def __str__(self):
        return f"Name: {self.firstName}\n Email: {self.email}\n Customer ID: {self.cust_id}"

if __name__ == "__main__":
    #__str__
    person = Person("Joel","Murach","12334@murach.com")
    print(person)
    customer = Customer("Frank","Wilson","frank@gmail.com","23432434")
    print(customer)
    employee = Employee("John","Apple","Johnapple123.com","324-343-434")
    print(employee)
    ##
    if isinstance(customer,Customer):
        print(f"Customer\n{customer}")
    if isinstance(employee,Employee):
        print(f"Employee\n{employee}")

