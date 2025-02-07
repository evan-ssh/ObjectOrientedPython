import random
class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def generateRoshambo(self):
        self.hand = "rock"

    def __str__(self):
        return self.name

    def play(self,opponent):
        if self.hand == opponent.hand:
            return None
        elif self.hand == "paper" and opponent.hand == "rock" or self.hand == "rock" and opponent.hand == "scissors" or self.hand == "scissors" and opponent.hand == "paper":
            return self
        else:
            return opponent
    
class Bart(Player):
    def  __init__(self):
        Player.__init__(self,"Bart","")
        self.generateRoshambo()

class Lisa(Player):
    def __init__(self):
        Player.__init__(self,"Lisa","")
        self.generateRoshambo()
    
    def generateRoshambo(self):
        ListOfHands = ["rock","paper","scissors"]
        self.hand = random.choice(ListOfHands)

if __name__ == "__main__":
 opponent = input("Who Would You Like To Face For An Opponent Bart or Lisa?")
 if opponent == "Bart":    
    player = Player("player", "rock")
    bart = Bart()
    print(f"Player Hand: {player.hand}")
    print(f"Barts Hand: {bart.hand}")
    winCase = player.play(bart)
    if winCase == None:
        print("Its a tie")
    else:
        print(f"{winCase} Wins With Hand {winCase.hand}")

 elif opponent == "Lisa":
    player = Player("player", "rock")
    lisa = Lisa()
    print(f"Player Hand: {player.hand}")
    print(f"Lisa's Hand: {lisa.hand}")
    winCase = player.play(lisa)
    if winCase == None:
        print("Its a tie")
    else:
        print(f"{winCase} Wins With {winCase.hand}")
