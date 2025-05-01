class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def isEmpty(self):
        return len(self.stack) == 0

def isBalanced(s):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.isEmpty() or stack.pop() != pairs[char]:
                return False
    return stack.isEmpty()

def main():
    brackets = input("Enter a string of parentheses/brackets: ")
    if isBalanced(brackets):
        print("Balanced!")
    else:
        print("Not balanced.")

if __name__ == "__main__":
    main()