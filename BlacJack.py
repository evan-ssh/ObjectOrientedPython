class Card:
    def __init__(self,suit,face,value,is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace
    def show_card(self):
        return(f"{self.face} of {self.suit}")
        