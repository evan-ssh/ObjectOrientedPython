class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
def serveCustomer(console,customers):
    stack = Stack()
    queue = Queue()
    for char in console:
        stack.push(char)
    for cust in customers:
        queue.enqueue(cust)

    while not queue.isEmpty() and not stack.isEmpty():
        served = False#Used to track rotations
        for _ in range(queue.size()):
            if queue.peek() == stack.peek():
                queue.dequeue() #Remove customer from queue
                stack.pop() #Remove console from stack
                served = True #Mark that a customer was served
                break
            else:
                queue.enqueue(queue.dequeue()) #Move customer to back of queue 'Rotate'
        if not served:#By the end of the rotations if served wasnt set to true break out and return remaining customers
            break
    return queue.size()
    
def main():
    console = ['X','X','X','P','P','X','P','X','P','X','P','P','P']
    customers = ['X','P','X','P','P','X','X','P','P','X','X','X','X']
    unable_to_buy = serveCustomer(console,customers)
    print(f"There are {unable_to_buy} customer(s) who were unable to purchase a console")
if __name__ == "__main__":
    main()