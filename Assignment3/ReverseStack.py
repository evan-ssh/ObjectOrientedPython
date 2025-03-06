class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
    
    def reverse(self):
        self.stack.reverse()
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
        return f"Stack Items: {self.stack}"
def main():

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
        print(stack)
        stack.reverse()
        print(stack)
main()