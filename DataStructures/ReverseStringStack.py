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
    
    def reverseStr(self,chars):
        for i in chars:
            self.push(i)
            
        reversedChars = []
        for i in range(len(self.stack)):
            i = self.pop()
            reversedChars.append(i)
        
        for i in range(len(reversedChars)):
            i = reversedChars.pop(0)
            self.push(i)
        print(self.stack)


def main():
    stack = Stack()
    chars = input("Enter a word")
    stack.reverseStr(chars)

if __name__ == "__main__":
    main()