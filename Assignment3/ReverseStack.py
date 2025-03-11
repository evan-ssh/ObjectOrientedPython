class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
    
    def reverse(self,chars):
        for char in chars:
            self.push(char)
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
        chars = ["a","b","c"]
        print(f"characters {chars}")
       
        stack.reverse(stack)
        print(stack)

if __name__ == "__main__":
    main()
