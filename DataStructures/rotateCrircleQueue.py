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

def rotateQueue(cq, k):
    if cq.isEmpty():
        print("Queue is empty! Cannot rotate.")
        return

    for _ in range(k):
        item = cq.dequeue()
        cq.enqueue(item)

def main():
    size = int(input("Enter the size of the circular queue: "))
    cq = CircularQueue(size)
    for i in range(size):
        cq.enqueue(input(f"Enter element {i+1}: "))

    print("Original Queue:")
    cq.display()

    k = int(input("Enter the number of rotations: "))
    rotateQueue(cq, k)

    print("Rotated Queue:")
    cq.display()

if __name__ == "__main__":
    main()