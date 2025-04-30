class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

def isAnagram(word1, word2):
    if len(word1) != len(word2):
        return False

    stack1 = Stack()
    stack2 = Stack()

    for char in sorted(word1):
        stack1.push(char)
    for char in sorted(word2):
        stack2.push(char)

    while not stack1.isEmpty():
        if stack1.pop() != stack2.pop():
            return False
    return True

def main():
    w1 = input("Enter first word: ")
    w2 = input("Enter second word: ")
    if isAnagram(w1, w2):
        print("Anagrams!")
    else:
        print("Not anagrams.")

if __name__ == "__main__":
    main()