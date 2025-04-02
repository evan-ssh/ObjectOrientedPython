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

   def addLast(self, newdata):
       NewNode = Node(newdata)
       if self.__headVal == None:
           self.__headVal = NewNode
       else:
           current = self.__headVal
           while current.nextval != None:
              current = current.nextval
           current.nextval = NewNode

 
   def listprint(self):
       printval = self.__headVal
       while printval is not None:
           print(printval.dataval)
           printval = printval.nextval

   def length(self):
        current = self.__headVal
        count = 0
        while current is not None:
            count += 1
            current = current.nextval
        return count



if __name__ == "__main__":
    list = LinkedList()

    list.addLast("Mon")
    list.addLast("Tues")
    list.addLast("Wed")

    list.listprint()