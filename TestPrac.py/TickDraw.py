import random
class DrawPrize:
    def __init__(self,lowNum,highNum,prize):
        self.prize = prize
        self.lowNum = lowNum
        self.highNum = highNum
        self.tickets = []
        self.winningTicket = None #Setting to none allows for us to inititalize  without needing this
        self.userTicket = []

    def createTickets(self):
        for i in range(self.lowNum,self.highNum+1):
            self.tickets.append(i)
    def setWinningTicket(self):
        if len(self.tickets) == 0:
            return 'No more tickets left Good Luck Next Time'
        self.winningTicket = random.choice(self.tickets)
    
    def giveTicket(self,amount):
        if len(self.tickets) == 0:
            return 'No more tickets left'
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

    def __iter__(self):
        for ticket in self.tickets:
            yield ticket

prize = DrawPrize(1,10,"Monkey")
prize.createTickets()
prize.setWinningTicket()
print("Tickets")
for tickets in prize:
    print(f"Ticket{tickets}")

while True:
    amount = int(input("Enter amount of tickets to buy:"))
    tickets = prize.giveTicket(amount)
    if tickets == "No more tickets left":
        print(tickets)
        break
    print(f"Tickets given: {tickets}")
    for ticket in tickets:
        winCase = prize.checkTicket(ticket)
        print(winCase)
 

