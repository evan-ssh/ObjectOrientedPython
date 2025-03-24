class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()#Place holder to point to first element in list


    def append(self,data):
        newNode = Node(data)
        curr = self.head
        while curr.next != None: #If it equals none then we are at the end
            curr = curr.next
        curr.next = newNode

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1 
            curr = curr.next
        return total
    
    def display(self):
        elems = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            elems.append(curr.data)
        return ', '.join(map(str,elems))

    def get(self, index): #Extract data from specific index
        if index >= self.length():
            print("Out of range error")
            return None
        curr_idx = 0
        curr = self.head
        while True:
            curr = curr.next
            if curr_idx == index:
                return curr.data
            curr_idx += 1

    def erase(self,index): #Erase node at index
        if index >= self.length():
            print("Out of range Error")
            return None
        curr_idx = 0
        curr = self.head
        while True:
            lastNode = curr
            curr = curr.next
            if curr_idx == index:
                lastNode.next = curr.next
                return
            curr_idx += 1

if __name__ == "__main__":
    myList = LinkedList()

    myList.display()

    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.append(5)
    myList.append(6)

    print(myList.display())
    print(f"Element at index 0 is {myList.get(0)}")

    myList.erase(1)
    print(myList.display())