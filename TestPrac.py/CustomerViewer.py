import csv
class Customer:
    def __init__(self,cust_id,first_name,last_name,company_name,address,city,state,zip):
        self.cust_id = cust_id
        self.first_name = first_Name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
    

def CustomerData():
    customerData = []
    filename = 'customers.csv'
    with open(filename) as file:
        for line in file:
         customerData.append(line)
    return customerData

customer = Customer(CustomerData())
for data in customerData:
    print(data)

