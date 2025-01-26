import random
class Card:
    def __init__(self,suit,face,value,is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace
    def show_card(self):
        return(f"{self.face} of {self.suit}")

class Deck:
    values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","King","Queen"]
    suits = ["Hearts", "Diamonds","Spades","Clubs"]

    def __init__(self):
        self.cards = []
        self.shuffle_deck()
    
    def create_deck(self):
        for face in self.values:
            for suit in self.suits:
                if face =="Ace":
                    value = 11
                    is_ace = True
                elif face == "Jack" or "King" or "Queen":
                    value = 10
                    is_ace = False
                else:
                    value = int(face)
                    is_ace = False
                self.cards.append(Card(suit,face,value,is_ace))
        
    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []
    
    def add_hand(self,card):
        self.hand.append(card)

    def hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            value += card.value
            if card.is_ace:
                aces += 1
        while value > 21 and aces:
            value - 10
            aces - 1
        return value