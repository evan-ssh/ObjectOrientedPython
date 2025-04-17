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
    player1Stack = Stack()
    player2Stack = Stack()
    for move in player1Moves:
        player1Stack.push(move)

    for move in player2Moves:
        player2Stack.push(move)
    while not player1Stack.isEmpty() and not player2Stack.isEmpty():
        player1Move = player1Stack.peek()
        player2Move = player2Stack.peek()
        if player1Move == player2Move:
            player1Stack.pop()
            player2Stack.pop()
            print("Its a tie!")
        elif (player1Move == "R" and player2Move == "S") or (player1Move == "S" and player2Move == "P") or (player1Move == "P" and player2Move == "R"):
            player1Stack.pop()
            player2Stack.pop()
            print(f"Player 1 wins {player1Move} beats {player2Move}")
        else: 
            player1Stack.pop()
            player2Stack.pop()
            print(f"Player 2 wins {player2Move} beats {player1Move}")
    if player1Stack.isEmpty() and player2Stack.isEmpty():
        print("The game ends in a tie!")
    elif player1Stack.isEmpty():
        print("Player 2 wins the game!")
    else:
        print("Player 1 wins the game!")
player1Moves = ["R","P","S"]
player2Moves = ["S","R","P"]
rpsGame(player1Moves,player2Moves)