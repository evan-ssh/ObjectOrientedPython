import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def show_card(self):
        return f"{self.rank} of {self.suit}"
        