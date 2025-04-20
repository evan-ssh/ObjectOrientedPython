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
    
    def isEmpty(self):
        return len(self.stack) == 0
    
def rpsGame(player1Moves,player2Moves):
    p1stack = Stack()
    p2stack = Stack()
    for move in player1Moves:
        p1stack.push(move)
    for move in player2Moves:
        p2stack.push(move)
    while not p1stack.isEmpty() and not p2stack.isEmpty():
        if p1stack.peek() == p2stack.peek():
            p1stack.pop()
            p2stack.pop()
        elif (p1stack.peek() == "R" and p2stack.peek() == "S") or (p1stack.peek() == "P" and p2stack.peek() == "R") or (p1stack.peek() == "S" and p2stack.peek() == "P"):
            p1stack.pop()
        else:
            p2stack.pop()
    if p1stack.isEmpty() and p2stack.isEmpty():
        return "It's a tie!"
    elif p1stack.isEmpty():
        return "Player 1 Wins!"
    else:
        return "Player 2 Wins!"
player1Moves = ["R","P","S"]
player2Moves = ["S","R","P"]
rpsGame(player1Moves,player2Moves)