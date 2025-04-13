class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.__headVal = None

    def add(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.__headVal
        self.__headVal = NewNode

    def listprint(self):
        printval = self.__headVal
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def findEven(self):
        evenCounter = 0
        currNode = self.__headVal
        while currNode != None:
            if currNode.dataval % 2 == 0:
                evenCounter += 1
                currNode = currNode.nextval
            else:
                currNode = currNode.nextval
        return evenCounter

    def findOdd(self):
        oddCounter = 0
        currNode = self.__headVal
        while currNode != None:
            if currNode.dataval % 2 == 1:
                oddCounter += 1
                currNode = currNode.nextval
            else:
                currNode = currNode.nextval
        return oddCounter

def main():
    
    list = LinkedList()
    while True:
        number = int(input("Enter the number to store in the linked list"))
        if number == -99:
            break
        else:
            list.add(number)
    print(f"The number of even values in the list is: {list.findEven()}")
    print(f"The number of odd values in the list is: {list.findOdd()}")
if __name__ == "__main__":
    main()

