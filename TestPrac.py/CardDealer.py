class Card:
    rank = ['1','2','3','4','5','6','7','8','9','10','Jacks','Queen','King']
    suite = ['Hearts','Diamonds','Clubs','Spades']
    def __init__(self,rank,suite):
        self.rank = rank
        self.suite = suite
       
    

    def __str__(self):
        return f"{self.rank} of {self.suite}"
        


class Deck:
    def __init__(self):
        self.DeckOfCards = []
    
    def generateDeck(self):
        for rank in Card.rank:
            for suit in Card.suite:
                self.DeckOfCards.append(Card(rank,suit))
    
    def amountCards(self):
        return len(self.DeckOfCards)
    
    def dealCard(self):
        self.DeckOfCards.pop()
    
    def __iter__(self):
        for card in self.DeckOfCards:
            yield card


deck = Deck()
deck.generateDeck()
for card in deck:
    print(card)
