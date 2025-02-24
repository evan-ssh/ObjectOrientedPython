#FIFO First In First Out

#Simple queue

class Queue:
    def __init__(self):
        self.customerLine = []

    def enqueue(self,customer):
        self.customerLine.append(customer)