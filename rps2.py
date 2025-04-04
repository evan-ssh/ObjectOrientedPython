import random
class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
        self.score = {"wins":0,"losses":0,"ties":0}
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
        
    def updateScore(self,winCase):
        if winCase == None:
            self.score['ties'] += 1
        elif winCase == self:
            self.score['wins'] += 1
        else:
            self.score['losses'] += 1
        

    def scoreBoard(self):
        print(f"-=SCOREBOARD=-\nWINS:{self.score['wins']}\nLOSSES:{self.score['losses']}\nTIES{self.score['ties']}\n")
    
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

class Elon(Player):
    def __init__(self,playersHand):
        Player.__init__(self,"Elon", "")
        self.generateRoshambo(playersHand)
    def generateRoshambo(self,playersHand):
        if playersHand == "rock":
            self.hand = "paper"
        elif playersHand == "paper":
            self.hand = "scissors"
        elif playersHand == "scissors":
            self.hand = "rock"

if __name__ == "__main__":
    opponent = input("Who Would You Like To Face For An Opponent Bart,Lisa or Elon?").lower()
    if opponent[0] == "b":    
        player = Player("player", "rock")
        bart = Bart()
        print(f"Player Hand: {player.hand}")
        print(f"Barts Hand: {bart.hand}")
        winCase = player.play(bart)
        if winCase == None:
            print("Its a tie")
        else:
            print(f"{winCase} Wins With Hand {winCase.hand}")
    elif opponent[0] == "l":
        player = Player("player", "rock")
        lisa = Lisa()
        print(f"Player Hand: {player.hand}")
        print(f"Lisa's Hand: {lisa.hand}")
        winCase = player.play(lisa)
        player.updateScore(winCase)
        if winCase == None:
            print("Its a tie")
            player.scoreBoard()
        else:
            print(f"{winCase} Wins With {winCase.hand}")
            player.scoreBoard()
    elif opponent[0] == "e":
        player = Player("player","rock")
        playersHand = player.hand
        elon = Elon(playersHand)
        print(f"Player Hand: {player.hand}")
        print(f"Elon's Hand: {elon.hand}")
        winCase = player.play(elon)
        player.updateScore(winCase)
        if winCase == None:
            print("Its a tie")
            player.scoreBoard()
        else:
            print(f"{winCase} Wins With {winCase.hand}")
            player.scoreBoard()
