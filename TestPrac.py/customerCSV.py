import csv
class Customer:
    def __init__(self,cust_id,first_name,last_name,company_name,address,city,state,zip):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city 
        self.state = state
        self.zip = zip

    def __str__(self):
        return f"Name:{self.cust_id}\nLastName:{self.last_name}\nCompany{self.company_name}"

        
def openFile():
    filename = 'customers.csv'
    customers = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            cust_id = row[0]
            first_name = row[1]
            last_name = row[2]
            company_name = row[3]
            address = row[4]
            city = row[5]
            state = row[6]
            zipcode = row[7]
            customer = Customer(cust_id,first_name,last_name,company_name,address,city,state,zipcode)
            customers.append(customer)
    return customers

