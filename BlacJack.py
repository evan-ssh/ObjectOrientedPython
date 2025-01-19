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