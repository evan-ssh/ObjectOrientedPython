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
            new_node.pointer = self.head #Set nodes pointer as self.head
            self.head = new_node #Make new node the head 


    def append(self,data):
        new_node = Node(data)
        if not self.head: #If list is empty
            self.head = new_node
        else:
            curr = self.head #Set current node to self.head 
            while curr.next: #Traverse list until the final node is reached
                curr = curr.next
            curr.next = new_node #Set last node pointer to the new node 

    def delete(self,data):
        if not self.head:
            print("List is empty")

        if self.head.data == data: #If the node to be deleted is the head
            self.head = self.head.pointer #Set the head to the next node

        curr = self.head
        while curr.pointer and curr.pointer.data != data:
            curr = curr.pointer

        if curr.pointer:
            curr.pointer = curr.pointer.pointer
        else:
            print(f"Node {data} could not be found")