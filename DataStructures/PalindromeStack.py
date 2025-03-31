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
        for char in chars:
            self.push(char)

        reversestr = ""
        while len(self.stack) > 0:
            i = self.pop()
            reversestr += i
        if chars == reversestr:
            print("Palindrome")
        else:
            print("Not  a palindrome")
        
def main():
    stack = Stack()
    while True:
        chars = input("Enter word to check if its a palindrome")
        stack.reverseStr(chars)

if __name__ == "__main__":
    main()