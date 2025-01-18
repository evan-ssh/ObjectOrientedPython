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