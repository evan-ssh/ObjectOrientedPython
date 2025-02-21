import random
class Tickets:
    def __init__(self,lowNum,highNum,prize):
        self.lowNum = lowNum
        self.highNum = highNum
        self.prize = prize
        self.tickets = []
        self.winningTicket = None
        self.userTicket = []

    def genrateTickets(self):
        for i in range(self.lowNum,self.highNum+1):
            self.tickets.append(i)
        
    def setWinningTicket(self):
        self.winningTicket = random.choice(self.tickets)

    def giveTicket(self,amount):
        for _ in range(amount):
            ticket = random.choice(self.tickets)
            self.tickets.remove(ticket)
            self.userTicket.append(ticket)
        return self.userTicket
    
    def amountTicket(self):
        return len(self.tickets)
    
    def checkTicket(self,ticket):
        if ticket == self.winningTicket:
            False
            return f"Ticket {ticket} is a winner {self.prize}"
        else:
            return f"Ticket {ticket} is not a winner :(("
    
prizes = random.choice(["sage","Rainbow Sage","Lemur"])
prize = Tickets(1,10,prizes)
prize.genrateTickets()
prize.setWinningTicket()
while True:
    if prize.amountTicket() == 0:
        print("No more tickets left Good Luck Next Time")
        break
    amount = int(input("Enter amount of tickets to buy:"))
    tickets = prize.giveTicket(amount)
    print(f"Tickets given: {tickets}")
    for ticket in tickets:
        winCase = prize.checkTicket(ticket)
        print(winCase)