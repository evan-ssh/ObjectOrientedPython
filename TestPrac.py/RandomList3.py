import random
class RandomIntList(list):
    def __init__(self):
        list().__init__()
    
    def __str__(self):
        return ', '.join(map(str,self))
    def genInts(self,amount):
        for _ in range(amount):
            self.append(random.randint(1,100))
    def count(self):
        count = 0
        for i in self:
            count += 1
        return count
    def total(self):
        total = 0
        for i in self:
            total += i
        return total

    def average(self):
        total = 0
        for i in self:
            total += i
        return total / len(self)
    def dealNum(self):
        return self.pop()
    
    def amountInt(self):
        return len(self)
        
class User:
    def __init__(self):
        self.userHand = []

    def giveNum(self,amount):
        for _ in range(amount):
            num = randomintlist.dealNum()
            self.userHand.append(num)
    
    def __str__(self):
        return ', '.join(map(str,self.userHand))
    
user = User()
randomintlist = RandomIntList()
amount = int(input("enter amount"))
randomintlist.genInts(amount)
print(f"Integers {randomintlist}")
print(f"Count {randomintlist.count()}")
print(f"Total {randomintlist.total()}")
print(f"Average {randomintlist.average()}")
while True:
    amountRandom = randomintlist.amountInt()
    if amountRandom == 0:
        print("Sorry there is no more numbers to request")
        break
    amount = int(input("Enter amount of numbers you'd like to recieve"))
    user.giveNum(amount)
    print(f"Users List\n{'='*10}")
    print(user)