from rps2 import Player,Bart,Lisa
def main():
    print("Roshambo Game")
    playerName = input("\nEnter your name: ")
    while True:
        chooseOpponent = input("\nWould you like to play against Bart or Lisa? ").lower()
        if chooseOpponent[0] == "b":
            chooseHand = input("\nRock, Paper, or Scissors? (r/p/s):").lower()
            if chooseHand[0] == "r":
                chooseHand = "rock"
            elif chooseHand[0] == "p":
                chooseHand = "paper"
            elif chooseHand[0] == "s":
                chooseHand = "scissors"
            else:
                print("Please choose rock, paper, or scissors")
                continue

            player = Player(playerName, chooseHand)
            bart = Bart()
            print(f"{player.name}: {player.hand}!")
            print(f"{bart.name} {bart.hand}!")
            winCase = player.play(bart)
            if winCase is None:
                print("It's a draw!")
            elif winCase == player:
                print(f"{player.name} wins!")
            else:
                print(f"{bart.name} wins!")
            playAgain = input("\nWould you like to play again? (y/n): ")
            if playAgain.lower() != "y":
                print("Thanks for playing!")
                break
        elif chooseOpponent[0] == "l":
            chooseHand = input("Rock, Paper, or Scissors? (r/p/s):").lower()

            if chooseHand[0] == "r":
                chooseHand = "rock"
            elif chooseHand[0] == "p":
                chooseHand = "paper"
            elif chooseHand[0] == "s":
                chooseHand = "scissors"
            else:
                print("Please choose rock, paper, or scissors")
                continue
            player = Player(playerName, chooseHand)
            lisa = Lisa()
            print(f"{player.name}: {player.hand}")
            print(f"{lisa.name}: {lisa.hand}")
            winCase = player.play(lisa)
            if winCase is None:
                print("It's a draw!")
            elif winCase == player:
                print(f"{player.name} wins!")
            else:
                print(f"{lisa.name} wins!")
            playAgain = input("Would you like to play again? (y/n): ")
            if playAgain.lower() != "y":
                print("Thanks for playing!")
                break
        else:
            print("Please pick an opponent")

if __name__ == "__main__":
    main()