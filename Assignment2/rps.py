class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

class Bart(Player):
    def  __init__(self):
        Player.__init__(self,"Bart","")
        