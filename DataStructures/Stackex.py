
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if len(self.stack) == 0:
            print("Error: Stack is empty. Nothing to peek.")
            return None
        return self.stack[-1]
    def display(self):
        for i in self.stack:
            print(i, end='')
        
def Mirror(stack):
    reverseStack = []
    for i in stack.stack:
        reverseStack.append(i)
    reverseStack.reverse()
    for i in reverseStack:
        stack.push(i)

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Original")
    stack.display()

    Mirror(stack)
    print("\nFlipped")
    stack.display()

    
if __name__ == "__main__":
    main()