import random
class List:
    def __init__(self):
        self.integers = []

class RandomIntList(List):
    def __init__(self,number_of_ints):
        List.__init__(self)
        self.addInt(number_of_ints)

    def addInt(self,number_of_ints):
        for i in range(number_of_ints):
            self.integers.append(random.randint(1,100))
    
    def show(self):
        return ','.join(map(str,self.integers))
    
    def count(self):
        return len(self.integers)
    
    def totalSum(self):
        total = 0
        for i in self.integers:
            total += i
        return(total)

    def average(self):
        total = 0
        for i in self.integers:
            total += i
        return (total/len(self.integers))

if __name__ == "__main__":
    randlist = RandomIntList(12)
    print(randlist.show())
    print(randlist.count())
    print(randlist.totalSum())
    print(randlist.average())