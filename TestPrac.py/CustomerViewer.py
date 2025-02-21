class Customer:
    def __init__(self,id,firstName,lastName,companyName,address,city,state,zip):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.companyName = companyName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
    

customerData = []  
filename = 'customers.csv'
with open(filename) as file:
    for line in file:
        customerData.append(line)

for data in customerData:
    print(data)

