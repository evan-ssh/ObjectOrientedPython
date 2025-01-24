import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def show_card(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suits = ["Hearts", "Diamonds","Spades","CLubs"]
    def __init__(self):
        self.cards = []