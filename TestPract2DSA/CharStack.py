class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()
    
    def add(self,char):
        self.stack.append(char)

    def length(self):
        return len(self.stack)
    
    def display(self):
        return ", ".join(map(str,self.stack))
    
def main():
    stack = Stack()
    while True:
        char = input("Enter a character: ")
        if char == '%':
            break
        stack.add(char)
    reversedStack = []
    while stack.length() > 0:
        reversedStack.append(stack.pop())
    for char in reversedStack:
        stack.add(char)
    print(stack.display())
            

    
        
    

main()