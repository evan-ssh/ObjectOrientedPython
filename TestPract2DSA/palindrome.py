class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.append(data)
    
    
    def dequeue(self):
        return self.queue.pop(0)
    def length(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,char):
        self.stack.append(char)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)


def isPalidrome(word):
    queue = Queue()
    stack = Stack()
    q = ""
    s = ""
    for char in word:
        queue.enqueue(char)
        stack.push(char)
    for _ in range(queue.length()):
        char = queue.dequeue()
        q += char
    for _ in range(stack.length()):
        char = stack.pop()
        s += char
    if q == s:
        return True
    else:
        return False
def main():
    word = input("Enter a word to check if its a palindrome")
    palindrome = isPalidrome(word)
    if palindrome:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
main()