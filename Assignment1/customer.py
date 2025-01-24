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

    def open_file():
        customers = []
        with open('customers.csv') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                customer = Customer(cust_id = row['cust_id'].strip(),first_name = row['first_name'].strip(), last_name = row['last_name'].strip(),company_name = row['company_name'].strip(),address = row['address'].strip(), city = row['city'].strip(), state = row['state'].strip(), zip = row['zip'].strip())
                customers.append(customer)
        return customers

    def customer_info(self):
        if self.company_name:
            return f"{self.first_name},{self.last_name}\n{self.company_name}\n{self.address}\n{self.city},{self.state},{self.zip}"
        else:
            return f"{self.first_name},{self.last_name}\n{self.address}\n{self.city},{self.state},{self.zip}"

    def customer_by_id(customers,customer_id):
        for customer in customers:
            if customer.cust_id == customer_id:
                return customer
        return None

if __name__ == "__main__":
    customers = Customer.open_file()
    customer_id = input("Enter customer ID:").strip()
    customer = Customer.customer_by_id(customers, customer_id)
    if customer:
        print(customer.customer_info())
    else:
        print("No customer with that id")
