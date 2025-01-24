from cards import Card,Deck,Player
deck = Deck()
player = Player()

while True:
    
    number_of_cards = int(input("How many cards would u like"))
    player.draw_card(deck,number_of_cards)
    player.show_hand()
    print(f"Remaing cards in deck: {deck.count_cards()}")
    if len(deck.cards) == 0:
        print("No more cards in deck!\n")
        choice = input("Draw more cards? (y/n)").lower().strip()
        if choice != "y":
            break