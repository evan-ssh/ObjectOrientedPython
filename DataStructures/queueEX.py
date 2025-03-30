class Queue:
    def __init__(self):
        self.queue = []

    def enqueue (self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) < 0:
            print("Cannot dequeue from empty queue")
        element = self.queue.pop(0)
        return element
    

    def __str__(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return " -> ".join(map(str, self.queue))
    
def reverseQueue(queue):
    reverseQueue = []
    while len(queue.queue) > 0:
        element = queue.dequeue()
        reverseQueue.append(element)
    while len(reverseQueue) > 0:
        i = reverseQueue.pop()
        queue.enqueue(i)
    print(queue)
    
def displayMenu():
    print("------------------")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. DISPLAY QUEUE")
    print("4. Reverse queue")
    print("------------------")
def main():
    queue = Queue()
    while True:
        displayMenu()
        command = int(input("Enter a command"))
        if command == 1:
            data = input("Enter data")
            queue.enqueue(data)
        elif command == 2:
            element = queue.dequeue()
            print(f"{element} was removed from queue")
        elif command == 3:
            print(queue)
        elif command == 4:
            reverseQueue(queue)
if __name__ == "__main__":
    main()