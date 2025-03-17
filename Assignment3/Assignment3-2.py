class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
    
    def reverse(self,numbers):
        for num in numbers:
            self.push(num)

        reverseStack = []
        for _ in range(len(self.stack)):
            reverseStack.append(self.pop())
        self.stack = reverseStack

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
    stack = Stack()
    numbers = [1,2,3,4,5]
    print(f"Numbers: {numbers}")
    stack.reverse(numbers)
    print(stack)
if __name__ == "__main__":
    main()
