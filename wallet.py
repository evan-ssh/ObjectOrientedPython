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