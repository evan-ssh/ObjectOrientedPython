from company import Employee,Customer
def main():
     while True:
        print("\nCustomer/Employee Data Entry")
        data_entry = input("\nCustomer or Employee? (c/e):")
        if data_entry[0] == "c":
            print("\nDATA ENTRY")
            firstName = input("Enter first name:")
            lastName = input("Enter last name:")
            email = input("Enter email:")
            cust_id = input("Enter customer ID:")
            customer = Customer(firstName, lastName,email,cust_id)
            if isinstance(customer,Customer):
                print(f"\nCUSTOMER\n{customer}")
            go_again = input("Continue? (y/n):")
            if go_again != "y":
                print("GoodBye!")
                break
        elif data_entry[0] == "e":
            print("\nData Entry")
            firstName = input("Enter first name:")
            lastName = input("Enter last name:")
            email = input("Enter email:")
            ssn = input("Enter SSN:")
            employee = Employee(firstName, lastName, email, ssn)
            if isinstance(employee, Employee):
                print(f"\nEMPLOYEE\n{employee}\n")
            go_again = input("Continue? (y/n):")
            if go_again != "y":
                print("GoodBye!")
                break
        else:
            print("Choose Customer or Employee")



if __name__ == "__main__":
    main()