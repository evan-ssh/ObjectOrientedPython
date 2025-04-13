class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

def Showdown(player1moves, player2moves):
    
    player1stack = Stack()
    player2stack = Stack()

    for move in (player1moves):
        player1stack.push(move)
    for move in (player2moves):
        player2stack.push(move)

    while not player1stack.is_empty() and not player2stack.is_empty():
        move_1 = player1stack.peek()  # Player 1's move
        move_2 = player2stack.peek()  # Player 2's move

        if move_1 == move_2:
            player1stack.pop()
            player2stack.pop()
        elif (move_1 == 'R' and move_2 == 'S') or (move_1 == 'S' and move_2 == 'P') or (move_1 == 'P' and move_2 == 'R'):
            player2stack.pop()
        else:
            player1stack.pop()

    if player1stack.is_empty() and player2stack.is_empty():
        return "Draw"
    elif player1stack.is_empty():
        return "Player B Wins"
    else:
        return "Player A Wins"

def main():
    player1moves = ['R', 'P', 'S']
    player2moves = ['S', 'R', 'P']
    print(f"{Showdown(player1moves, player2moves)}")
   
if __name__ == "__main__":
    main()