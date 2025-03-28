class Node:
    def __init__(self,data):
        self.pointer = None
        self.data = data
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def InsertBeginning(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.pointer = self.head 
            self.head = new_node 


    def AddEnd(self,data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
        else:
            curr = self.head 
            while curr.pointer: 
                curr = curr.pointer
            curr.pointer = new_node 

    def Delete(self,data):
        if not self.head:
            print("List is empty")

        if self.head.data == data: 
            self.head = self.head.pointer 

        curr = self.head
        while curr.pointer and curr.pointer.data != data:
            curr = curr.pointer

        if curr.pointer:
            curr.pointer = curr.pointer.pointer
        else:
            print(f"Node {data} could not be found")
 
    def Show(self):
        curr = self.head 
        while curr: 
            print(curr.data, end=" | ") 
            curr = curr.pointer 
        