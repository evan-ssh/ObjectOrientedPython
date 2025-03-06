

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def deque(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:                
            return "Cannot remove from empty queue"
    def length(self):
        return len(self.queue)
    def __str__(self):
        return f"Queue {self.queue}"


def mirror(queue):
    reversedList = []
    for char in queue.queue:
        reversedList.append(char)
    reversedList.reverse()
    for char in reversedList:
        queue.enqueue(char)
    

def main():
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
    print(queue)
    mirror(queue)
    print(queue)
main()