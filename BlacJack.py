import random
class Card:
    def __init__(self,suit,face,value,is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace
    def __str__(self):
        return f"{self.face} of {self.suit}"

class Deck:
    values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","King","Queen"]
    suits = ["Hearts", "Diamonds","Spades","Clubs"]

    def __init__(self):
        self.cards = []
        self.createDeck()
        self.shuffleDeck()
    
    def createDeck(self):
        for face in self.values:
            for suit in self.suits:
                if face =="Ace":
                    value = 11
                    is_ace = True
                elif face == "Jack" or face == "King" or face == "Queen":
                    value = 10
                    is_ace = False
                else:
                    value = int(face)
                    is_ace = False
                self.cards.append(Card(suit,face,value,is_ace))
        
    def shuffleDeck(self):
        random.shuffle(self.cards)
    
    def dealCard(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []
        handval = 0
    
    def addHand(self,deck):
        self.hand.append(deck.deal_card())
        self.handValue()

    def handValue(self):
        value = 0
        aces = 0
        for card in self.hand:
            value += card.value
            if card.is_ace:
                aces += 1
        if value > 21 and aces:
            value -= 10
            aces -= 1
        self.handval = value
    def showHand(self):
        return f", ".join(map(str,self.hand))

class Dealer(Player):
    def __init__(self):
        Player.__init__(self)
    

if __name__ == "__main__": 
    deck = Deck()
    player = Player()
    dealer = Dealer()
while True:
    for _ in range(2): 
        player.addHand(deck)
        dealer.addHand(deck)
    print(player.showHand())
    print(player.handValue())
    print(dealer.showHand())
    print(dealer.handValue())
    if player.handValue() > 21 or dealer.handValue > 21:
        print("")
    hitStand = input("would u like to hit or stand ")
    