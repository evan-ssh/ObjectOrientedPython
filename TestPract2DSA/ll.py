class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()


    def append(self,data):
        newNode = Node(data)
        curr = self.head
        while curr.next != None: 
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