import random
class RandomIntList(list):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return ', '.join(map(str,self))

    def genInts(self,amount):
        for _ in range(amount):
            self.append(random.randint(1,100))

    def amountInts(self):
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
    
randomintlist = RandomIntList()
amount = int(input("How many random integers should the list contain?: "))
randomintlist.genInts(amount)
print(f"Integers: {randomintlist}")
print(f"Count: {randomintlist.amountInts()}")
print(f"Total: {randomintlist.total()}")
print(f"Average {randomintlist.average()}")