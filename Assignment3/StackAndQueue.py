class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.pop
        
    def length(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        
    class Queue:
        def __init__(self):
            self.queue = []

        def enqueue(self, item):
            self.queue.append(item)
        def deque(self,item):
            if len(self.queue) != 0:
                return self.pop(0)
            else:
                return "Cannot remove from empty queue"