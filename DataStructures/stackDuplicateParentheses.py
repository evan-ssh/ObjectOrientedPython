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

def isDuplicate(expr):
    stack = Stack()
    for char in expr:
        if char == ')':
            top = stack.pop()
            elements_inside = 0
            while top != '(':
                elements_inside += 1
                top = stack.pop()
            if elements_inside == 0:
                return True 
        else:
            stack.push(char)
    return False

def main():
    expr = input("Enter an expression: ")
    if isDuplicate(expr):
        print("Duplicate parentheses found!")
    else:
        print("No duplicate parentheses.")

if __name__ == "__main__":
    main()