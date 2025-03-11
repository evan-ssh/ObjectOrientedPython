class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        
    def length(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        
    def clear(self):
        self.stack = []

    def __str__(self):
        return f"Stack Items: {len(self.stack)}"
        
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:                
            return "Cannot remove from empty queue"
    
    def peek(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:                
            return "Cannot remove from empty queue"

    def length(self):
        return len(self.queue)
    def __str__(self):
        f"Queue {len(self.queue)}"

def displayMenu():
    print("1. Start a stack")
    print("2. Start a queue")

def main():
    displayMenu()
    command = int(input("Enter a command:"))
    if command == 1:
        stack = Stack()
        i1 = "a"
        i2 = "b"
        i3 = "c"
        stack.push(i1)
        print(f"{i1} was added to stack")
        stack.push(i2)
        print(f"{i2} was added to stack")
        stack.push(i3)
        print(f"{i3} was added to stack")
        print(f"Is the stack empty? {stack.is_empty()}")
        print(f"Items in stack {stack.length()}")
        poppedItem = stack.pop()
        print(f"{poppedItem} was popped from stack")
        peekItem = stack.peek()
        print(f"{peekItem} was peeked from stack")
        print(stack)
    elif command == 2:
        queue = Queue()
        i1 = "a"
        i2 = "b"
        i3 = "c"
        queue.enqueue(i1)
        print(f"{i1} was added to the queue")
        queue.enqueue(i2)
        print(f"{i2} was added to the queue")
        queue.enqueue(i3)
        print(f"{i3} was added to the queue")
        print(f"There are {queue.length()} items in queue")
        peekItem = queue.peek()
        print(f"{peekItem} was returned from the front of the queue")
        dequeueItem = queue.dequeue()
        print(f"{dequeueItem} was returned from the end of the queue")
if __name__ == "__main__":
    main()
            