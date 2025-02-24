import csv
class Customer:
    def __init__(self,cust_id,first_name,last_name,company_name,address,city,state,zip)
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city 
        self.state = state
        self.zip = zip

    def __str__(self):
        return f"Name:{self.cust_id}\nLastName:{self.last_name}\nCompany{self.company_name}
