class Card:
    def __init__(self,rank,suite):
        self.rank = ['1','2','3','4','5','6','7','8','9','10','Jacks','Queen','King']
        self.suite = ['Hearts','Diamonds','Clubs','Spades']
    

    def __str__(self):
        return f"{self.rank} of {self.suite}"
        

