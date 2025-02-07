class Person():
    def __init__(Self,firstName,lastName,email):
        Self.firstName = firstName
        Self.lastName = lastName
        Self.email = email

    def FullName(self):
        return f"First Name: {self.firstName}\nLast Name: {self.lastName}\nEmail: {self.email}"
    

class Employee(Person):
    def __init__(self,firstName, lastName, email, ssn):
        Person.__init__(self,firstName,lastName,email)
        self.ssn = ssn
    
    def FullName(self):
        return f"Name: {self.firstName}\nEmail: {self.email}\nSSN: {self.ssn}"
    
    