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

randlist = RandomIntList(5)
print(randlist.show())