class Transaction:
    def __init__(self,title,amount,type):
        self.title = title
        self.amount = amount
        self.type = type
    def display_info(self):
        return f"|Transaction Details|\n |Expense{self.title}|\n |Amount: {self.amount}| \n |Expense Type{self.type}"