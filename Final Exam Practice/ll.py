class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.__headVal = None

    def add(self,newData):
        newNode = Node(newData)
        newNode.nextval = self.__headVal
        self.__headVal = newNode

    def listprint(self):
        printval = self.__headVal
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def search(self,target):
        currNode = self.__headVal
        while currNode:
            if currNode.dataval == target:
                return True
            currNode = currNode.nextval
        return False
    
def main():
    linkedlist = LinkedList()
    while True:
        num = int(input("Enter number to store in the list"))
        if num == -99:
            break
        else:
            linkedlist.add(num)
    print("The entered values are:")
    linkedlist.listprint()
    while True:
        searchNum = int(input("Enter the number to search for"))
        if searchNum == -99:
            break
        numFound = linkedlist.search(searchNum)
        if numFound:
            print(f"{searchNum} is contained in the list")
            continue
        else:
            print(f"{searchNum} is not contained in te list")
            continue
if __name__ == "__main__":
    main()