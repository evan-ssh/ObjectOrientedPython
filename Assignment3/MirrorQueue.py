

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def deque(self):
        if len(self.queue) != 0:
            return self.queue.pop()
        else:                
            return "Cannot remove from empty queue"
    
    def peek(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:                
            return "Cannot remove from empty queue"

    def length(self):
        return len(self.queue)
    def __str__(self):
        f"Queue {len(self.queue)}"


def mirror(queue):
    characters = ["a","b","c"]
    reversedList = []
    for char in characters:
        reversedList.append(char)
    reversedList.reverse()
    for char in reversedList:
        characters.extend(reversedList)
        break
    print(characters)

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
    mirror(queue)
main()