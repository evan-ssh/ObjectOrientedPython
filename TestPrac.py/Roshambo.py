class Player:
    def __init__(self,name,handVal):
        self.name = name
        self.handVal = handVal

    def generateRoshambo(self):
        self.handVal = "rock"
    
    def play(self,opponent):
        if self.handVal == opponent.handVal:
            return None
        if self.handVal == "rock" and opponent.handVal == "scissors" or self.handVal == "scissors" and opponent.handVal == "paper" or self.handVal == "paper" and opponent.handVal == "rock":
            return self
        else:
            return opponent

class Bart(Player):
    def __init__(self):
        super().__init__("Bart","rock")
        self.generateRoshambo()

    def generateRoshambo(self):
        self.handVal = "rock"

player = Player("player","rock")
bart = Bart()
wincase = player.play(bart)
if wincase == None:
    print("Its a tie")
else:
    print(wincase.name)