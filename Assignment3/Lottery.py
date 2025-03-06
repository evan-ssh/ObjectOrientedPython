import random
class Lottery:
    def __init__(self):
        self.winningNums = {9,20,27,35,37,43}
        self.randomNums = set()
        for _ in range(6):
            i = random.randint(1,49)
            if i not in self.randomNums:
                self.randomNums.add(i)
    def display(self):
        print(self.winningNums)
        print(self.randomNums)
    
lottery = Lottery()
lottery.display()