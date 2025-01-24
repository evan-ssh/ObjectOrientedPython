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

    def customer_info(self):
        if self.company_name:
            return f"{self.cust_id}\n{self.first_name},{self.last_name}\n{self.company_name}\n{self.address}\n{self.city},{self.state},{self.zip}"
        else:
            return f"{self.cust_id}\n{self.first_name},{self.last_name}\n{self.address}\n{self.city},{self.state},{self.zip}"

    def open_file(self):
        customers = []
        with open('customers.csv') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                customer = Customer(cust_id = row['cust_id'].strip(),first_name = row['first_name'].strip(), last_name = row['last_name'].strip(),company_name = row['company_name'].strip(),address = row['address'].strip(), city = row['city'].strip(), state = row['state'].strip(), zip = row['zip'].strip())
                customers.append(customer)
        return customers
        