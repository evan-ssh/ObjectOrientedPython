import random
class Tickets:
    def __init__(self,lowNum,highNum,prize):
        self.lowNum = lowNum
        self.highNum = highNum
        self.prize = prize
        self.tickets = []
        self.winningTicket = None
        self.userTicket = []


    def amountOfTickets(self):
        return len(self.tickets)

    def createTickets(self):
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
    
    def checkTicket(self,ticket):
        if ticket == self.winningTicket:
            return f"Ticket {ticket} is a Winner {self.prize}"
        else:
            return f"Ticket {ticket} is not a winning ticket :(("   
prizes = random.choice(["sage","Rainbow Sage","Lemur"])
prize = Tickets(1,10,prizes)
prize.createTickets()
prize.setWinningTicket()
while True:
    prize.amountOfTickets()
    if prize.amountOfTickets() == 0:
        print("No more tickets left Good Luck Next Time")
        break
    amount = int(input("Enter amount of tickets to buy:"))
    tickets = prize.giveTicket(amount)
    print(f"Tickets given: {tickets}")
    for ticket in tickets:
     winCase = prize.checkTicket(ticket)
     print(winCase)
