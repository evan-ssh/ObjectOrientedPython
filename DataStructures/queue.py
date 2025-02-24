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

def displayMenu():
    print("1. Add customer to line")
    print("2. Remove customer from line")
    print("3. Exit Program")

def main():
    queue = Queue()
    displayMenu()
    while True:
        command = int(input("Enter a command"))
        if command == 1:
            customer = input("Enter customer name")
            queue.enqueue(customer)
        elif command == 2:
            customer = queue.dequeue()
            print(f"{customer} was removed from the line")
    
main()