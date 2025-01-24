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
        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        for rank in self.ranks:
         for suit in self.suits:
            self.cards.append(Card(rank,suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)
    
    def pop_card(self):
        return self.cards.pop()

    def count_cards(self):
        return len(self.cards)

class Player:
    def __init__(self):
        self.hand = []

    def draw_card(self,deck,number_of_cards):
        for _ in range(number_of_cards):
            self.hand.append(deck.pop_card())
    
    def show_hand(self):
        print("Here are your cards:")
        for cards in self.hand:
            print(cards.show_card())

if __name__ == "__main__":
    deck = Deck()
    player = Player()
    number_of_cards = int(input("Num of cards to draw"))
    player.draw_card(deck,number_of_cards)
    player.show_hand()
    print(f"There are {deck.count_cards()} cards left in the deck\nGoodLuck!")