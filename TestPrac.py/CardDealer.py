class Card:
    rank = ['1','2','3','4','5','6','7','8','9','10','Jacks','Queen','King']
    suite = ['Hearts','Diamonds','Clubs','Spades']
    def __init__(self,rank,suite):#Define the lists outside then init
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
        return self.DeckOfCards.pop()
    
    def __iter__(self):
        for card in self.DeckOfCards:
            yield card

class Player:
    def __init__(self):
        self.hand = []
    def cardsInHand(self):
        if len(self.hand) == 0:
            return None
        return len(self.hand)
    def dealPlayer(self,deck,dealAmount):#Pass Deck Instance
        for card in range(dealAmount):
            card = deck.dealCard()
            self.hand.append(card)
    def __iter__(self):
        for card in self.hand:
            yield card

    
player = Player()
deck = Deck()
deck.generateDeck()
print(f"I have Shuffled a deck of {deck.amountCards()} Cards")
while True:
    dealAmount = int(input("How many cards would u like?: "))
    player.dealPlayer(deck,dealAmount)  
    print(f"Here are your cards:")
    for card in player:
     print(f"\n{card}")
    print(f"There are {deck.amountCards()} left in the deck")