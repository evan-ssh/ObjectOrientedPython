
from customer import Customer
while True:
    customers = Customer.open_file()
    customer_id = input("Enter Customer ID:").strip()
    customer = Customer.customer_by_id(customers,customer_id)

    if customer:
        print(customer.customer_info())
    else:
        print("No customer with that ID.")
    command = input("Search for another customer?(y/n):").strip().lower()
    if command != 'y':
        break