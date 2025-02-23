import random
class RandomIntList(list):#Creates the class as a list
    def __init__(self):
        super().__init__()

    def GenRandomInt(self,amount):#Dont pass in the instance
        for _ in range(amount):
         self.append(random.randint(1,100))# Dont forget to pass argueents to randint function

    def Count(self):
        count = 0
        for i in self:
            count += 1
        return count

    def Total(self):
        total = 0
        for i in self:
            total += i
        return total

    def Average(self):
        total = 0
        for i in self:
            total += i
        return total / len(self)

    def JoinInt(self):
        return ', '.join(map(str,self))#Dont forget to return

random_list = RandomIntList()
random_list.GenRandomInt(10)
print(f"List Count {random_list.Count()}")
print(f"Total {random_list.Total()}")
print(f"Average {random_list.Average()}")
print(random_list.JoinInt())