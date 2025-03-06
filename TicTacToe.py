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