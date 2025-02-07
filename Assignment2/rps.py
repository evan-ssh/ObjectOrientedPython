import random
class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def generateRoshambo(self):
        self.hand = "rock"
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