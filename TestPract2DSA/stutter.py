class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,num):
        self.queue.append(num)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Empty queue")
            return
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return ", ".join(map(str,self.queue))
    
def stutter(queue):
    size = queue.size()
    for _ in range(size):
        num = queue.dequeue()
        queue.enqueue(num)
        queue.enqueue(num)
    print(queue.display())
def displayMenu():
    print("1. Enter a num to queue")
    print("2. Stutter queue")
    print("3. Exit")

def main():
    queue = Queue()
    while True:
        displayMenu()
        command = int(input("Enter command: "))
        if command == 1:
            num = int(input("Enter a number to queue"))
            queue.enqueue(num)
        elif command == 2:
            stutter(queue)
        else:
            print("Goodbye")
            break

if __name__ == "__main__":
    main()