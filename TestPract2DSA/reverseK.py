class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,data):
        self.queue.append(data)
    
    def pop(self):
        return self.queue.pop(0)
    def display(self):
        return ", ".join(map(str,self.queue))
    def __len__(self):
        return len(self.queue)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def display(self):
        return ", ".join(map(str,self.stack))
    
def reverseK(queue, k):
    if k > len(queue) or k <= 0:
        print("Enter a valid number")
        return queue
    stack = Stack()

    for _ in range(k):
        stack.push(queue.pop())

    while len(stack.stack) > 0:
        queue.enqueue(stack.pop())
    for _ in range(len(queue.queue) - k):
        queue.enqueue(queue.pop())

    return queue

def main():
    queue = Queue()
    for i in [1, 2, 3, 4, 5]:
        queue.enqueue(i)

    print("Original Queue:", queue.display())
    k = int(input("Enter the number of elements to reverse (K): "))
    reverseK(queue, k)
    print("Modified Queue:", queue.display())

if __name__ == "__main__":
    main()
