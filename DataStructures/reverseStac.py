class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

def reverseWord(word):
    stack = Stack()
    for char in word:
        stack.push(char)
    reversed_word = ""
    while not stack.isEmpty():
        reversed_word += stack.pop()
    return reversed_word

def reverseEach(sentence):
    words = sentence.split()
    reversed_words = [reverseWord(word) for word in words]
    return " ".join(reversed_words)

def main():
    sentence = input("Enter a sentence: ")
    print(f"Reversed words:{reverseEach(sentence)}")

if __name__ == "__main__":
    main()