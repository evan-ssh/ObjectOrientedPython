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

        
def serveCustomer(console,customer):
    stack = Stack()
    queue = Queue()
    for char in console:
        stack.push(char)
    for cust in customer:
        queue.enqueue(cust)
    
    while not queue.isEmpty() and not stack.isEmpty():
        served = False
        for _ in range(queue.size()):
            if queue.peek() and stack.pop():
                queue.dequeue()
                stack.pop()
                served = True
                break
            else:
                queue.enqueue(queue.dequeue())
        if not served:
            break
    return queue.size()
def main():
    console = ['X','X','X','P','P','X','P','X','P','X','P','P','P']
    customers = ['X','P','X','P','P','X','X','P','P','X','X','X','X']
    unable_to_buy = serveCustomer(console,customers)
    print(f"There are {unable_to_buy} customer(s) who were unable to purchase a console")
if __name__ == "__main__":
    main()