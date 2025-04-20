
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
    def append(self, newdata):
        newNode = Node(newdata)
        if not self.__headVal:
            self.__headVal = newNode
            return
        curr = self.__headVal
        while curr.nextval:
            curr = curr.nextval
        curr.nextval = newNode
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

    def length(self):
        count = 0
        curr = self.__headVal
        while curr:
            count += 1
            curr = curr.nextval
        return count
    
    def reverse(self):
        prev = None
        curr = self.__headVal
        while curr:
            next_node = curr.nextval
            curr.nextval = prev
            prev = curr
            curr = next_node
        self.__headVal = prev
def main():
    linkedlist = LinkedList()
    while True:
        num = int(input("Enter number to store in the list: "))
        if num == -99:
            break
        else:
            linkedlist.add(num)
    print(f"The entered values are:")
    linkedlist.listprint()
    while True:
        searchNum = int(input("Enter the number to search for"))
        if searchNum == -99:
            break
        numFound = linkedlist.search(searchNum)
        if numFound == True:
            print(f"{searchNum} is contained in the list")
            continue
        else:
            print(f"{searchNum} is not contained in the list")
            continue
if __name__ == "__main__":
    main()