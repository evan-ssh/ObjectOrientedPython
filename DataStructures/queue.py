#FIFO First In First Out

#Simple queue

class Queue:
    def __init__(self):
        self.customerLine = []

    def enqueue(self,customer):
        self.customerLine.append(customer)
    
    def dequeue(self):
        if len(self.customerLine) != 0:
            return self.customerLine.pop(0)
        else:
            return "Cannot remove from an empty line"