class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full! Cannot add more items.")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! Cannot remove items.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:  
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

def main():
    size = int(input("Enter the size of the circular queue: "))
    cq = CircularQueue(size)

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter the item to enqueue: ")
            cq.enqueue(item)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.display()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()