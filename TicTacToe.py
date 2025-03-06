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