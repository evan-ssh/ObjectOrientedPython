from bank import Bank
def main():
    wallet = Bank()
    wallet.load_file()
    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add a Transaction")
        print("2. Remove a Transaction")
        print("3. Display All Transactions")
        print("4. Exit Program")
        print("======================================")

        command = input("Enter command")
        if command == "1":
            wallet.AddTransactionMain()
        elif command == "2":
            name = input("Enter Name of Transaction to Delete:")
            print(wallet.del_transaction(name))
        elif command == "3":
            print(wallet.display_transactions())
        elif command == "4":
            print("Exiting Finance Tracker")
            break
        else:
            print("Invalid Choice")
        
if __name__ == "__main__":
    main()