import json
class Transaction:
    def __init__(self,name,amount,type,note=""):
        self.name = name
        self.amount = amount
        self.type = type
        self.note = note
    def display_info(self):
        return f"|Transaction Details|\n |Expense{self.title}|\n |Amount: {self.amount}| \n |Expense Type{self.type}"
    

class Bank:
    def __init__(self):
        self.wallet = []

    def add_transaction(self,transaction):
        self.wallet.append(transaction)
    
    def del_transaction(self,name):
        for transaction in self.wallet:
            self.wallet.remove(transaction)
            return f"{name} has been removed"
        return f"{name} wasn't found"
    def display_transactions(self):
        if not self.wallet:
            return f"No transaction available in your wallet."
        return f"\n".join([transaction.display_info() for transaction in self.wallet])
    
    def load_file(self,filename="wallet.json"):
        try:
            with open(filename,"r") as file:
                transactions = json.load(file)
                self.wallet = [Transaction(transaction['Name'], transaction,['Amount'], transaction['Type'], transaction['Note']) for transaction in transactions]
        except FileNotFoundError:
            print("No file was found")

    def save_file(self,filename="wallet.json"):
        transactions = [{'Name': transaction.name, 'Amount': transaction.amount, 'Type': transaction.type, 'Note': transaction.note}]
        with open(filename,"w") as file:
            json.dump(transactions,file)
    
    def AddTransactionMain(self):
     while True:
      try:
          name = input("Enter name of transaction")
          amount = float(input("Enter amount"))
          type = input("Expense or Deposit?") 
          note = input("Leave a Note?")
          transaction = Transaction(name,amount,type,note)
          self.add_transaction(transaction)
          self.save_file()
          print(f"{name} added succesfully!")
          break
      except ValueError:
          print(f"Amount entered must be a number")

    
    