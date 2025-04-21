class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def reverse_stack(numbers):
    stack = Stack()
    for num in numbers:
        stack.push(num)
    reverseStack = []
    while not stack.isEmpty():
        reverseStack.append(stack.pop())
    return reverseStack
numbers = [1, 2, 3, 4, 5]
print(reverse_stack(numbers))