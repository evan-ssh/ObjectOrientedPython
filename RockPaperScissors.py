from rps2 import Player,Bart,Lisa,Elon
def main():
    print("Roshambo Game")
    playerName = input("\nEnter your name: ")
    player = Player(playerName, "")
    while True:
        chooseOpponent = input("\nWould you like to play against Bart,Lisa, or Elon? ").lower()
        if chooseOpponent[0] == "b":
         while True:
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

            player.hand = chooseHand 
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
            player.updateScore(winCase)
            player.scoreBoard()
            playAgain = input("\nWould you like to play bart again? (y/n): ")
            if playAgain.lower() != "y":
                print("Thanks for playing!")
                break
        elif chooseOpponent[0] == "l":
         while True:
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
            player.hand = chooseHand
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
            player.updateScore(winCase)
            player.scoreBoard()
            playAgain = input("Would you like to play Lisa again? (y/n): ")
            if playAgain.lower() != "y":
                print("Thanks for playing!")
                break

        elif chooseOpponent[0] == "e":
            while True:

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
                player.hand = chooseHand
                elon = Elon(player.hand)
                print(f"{player.name}: {player.hand}")
                print(f"{elon.name}: {elon.hand}")
                winCase = player.play(elon)
                if winCase is None:
                    print("It's a draw!")
                elif winCase == player:
                    print(f"{player.name} wins!")
                else:
                    print(f"{elon.name} wins!")
                playAgain = input("Would you like to play Lisa again? (y/n): ")
                if playAgain.lower() != "y":
                    print("Thanks for playing!")
                    break
        else:
            print("Please pick an opponent")

if __name__ == "__main__":
    main()