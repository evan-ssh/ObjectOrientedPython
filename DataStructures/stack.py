#FILO First in Last Out

#Simple stack
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
    
def main():
    stack = Stack()
    while True:
        name = input("Enter a name")
        if name == "%":
            break
        stack.push(name)
        print(f"{name} was added to the stack")
    for _ in range(stack.size()):
        person = stack.pop()
        print(person)
    print("Stack finished")
    
if __name__ == "__main__":
    main()