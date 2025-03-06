class Board:
    def __init__(self):
        self.board = [["_","_","_"],["_","_","_"],["_","_","_"]]

    def showBoard(self):
        print("_" * 7)
        for row in self.board:
            print("|" + "|".join(row) + "|") 
        
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