class Board:
    def __init__(self):
        self.board = [["_","_","_"],["_","_","_"],["_","_","_"]]

    def showBoard(self):
        print("_" * 7)
        for row in self.board:
            print("|" + "|".join(row) + "|")  