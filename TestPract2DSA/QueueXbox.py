class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,customer):
        self.queue.append(customer)

    def dequeue(self):
        customer = self.queue.pop(0)
        return customer
def displayMenu():
    print("1. Add customer")
    print("2. Process Customer")
    print("3. Exit")
def main():
    queue = Queue()
    while True:
        displayMenu()
        command = int(input("Enter a command"))
        if command == 1:
            customer = input("Enter customer")
            queue.enqueue(customer)
        elif command == 2:
            customer = queue.dequeue()
            print(f"{customer} was sold an Xbox")
        elif command == 3:
            print("Store closed")
            break

if __name__ == "__main__":
    main()