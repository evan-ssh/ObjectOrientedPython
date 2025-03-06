class Board:
    def __init__(self):
        self.board = [["_","_","_"],["_","_","_"],["_","_","_"]]

    def showBoard(self):
        print("_" * 7)
        for row in self.board:
            print("|" + "|".join(row) + "|") 
    def resetBoard(self):
        self.board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    def updateBoard(self,row,col,symbol):
        if self.board[row][col] == "_":
            self.board[row][col] = symbol
            return True
        else:
            return False

    def checkRows(self):
        # Horizontal lines
        for row in self.board:
            if row[0] == row[1] == row[2] != "_":
                return True
        # Vertical lines
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "_":
                return True
        # Diagonal lines
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "_" or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != "_":
            return True
        return False

class Player():
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
    def makeMove(self,board):
        while True:
            print(f"{self.name} it is your turn!")
            try:
                row = int(input("row:")) - 1
                col = int(input("col: ")) - 1
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Please enter a row and col 1-3")
                    continue
                if board.updateBoard(row,col,self.symbol):
                    board.showBoard()
                    break
                else:
                    print("That Space Is Taken!")
            except ValueError:
                print("Please enter a row and col 1-3")
    def __str__(self):
        return f"{self.name}"

def main():
    board = Board()
    player1name = input("PLAYER 1 Enter your name: ")
    player2name = input("PLAYER 2 Enter your name: ")
    player1symbol = input("PLAYER 1 Enter your symbol: ")
    player2symbol = input("PLAYER 2 Enter your symbol: ")
    player1 = Player(player1name,player1symbol)
    player2 = Player(player2name,player2symbol)
    round = 0
    while True:
        if round % 2 == 0:
            print(f"\nTicTacToe\nRound - {round+1}")
            board.showBoard()
            player1.makeMove(board)
            winCase = board.checkWin()
            if winCase == True:
                print(f"{player1} Wins!")
                go_again = input("Play Another Match?(y/n): ")
                if go_again == "y":
                    board.resetBoard()
                    round = 0
                    continue
                else:
                    print("Goodbye!")
                    break   
            elif winCase == board:
                print("Tie!")
                print(f"{player1} Wins!")
                go_again = input("Play Another Match?(y/n): ")
                if go_again == "y":
                    board.resetBoard()
                    round = 0
                    continue
                else:
                    print("Goodbye!")
                    break   
            round += 1
        elif round % 2 != 0:
            print(f"\nTicTacToe\nRound - {round+1}")
            board.showBoard()
            player2.makeMove(board)
            winCase = board.checkWin()
            if winCase == True:
                print(f"{player2} Wins!")
                go_again = input("Play Another Match?(y/n): ")
                if go_again == "y":
                    board.resetBoard()
                    round = 0
                    continue
                else:
                    print("Goodbye!")
                    break   
            elif winCase == board:
                print(f"Tie!")
                go_again = input("Play Another Match?(y/n): ")
                if go_again == "y":
                    board.resetBoard()
                    round = 0
                    continue
                else:
                    print("Goodbye!")
                    break   
            else:
                round += 1
main()