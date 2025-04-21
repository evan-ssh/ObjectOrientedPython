

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
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    print(queue)
    mirror(queue)
    print(queue)
if __name__ == "__main__":
    main()