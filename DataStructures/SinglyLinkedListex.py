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


    def AddEnd(self,data):
        new_node = Node(data)
        if not self.head: #If list is empty
            self.head = new_node
        else:
            curr = self.head #Set current node to self.head 
            while curr.pointer: #Traverse list until the final node is reached
                curr = curr.pointer
            curr.pointer = new_node #Set last node pointer to the new node 

    def Delete(self,data):
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
 
    def Show(self):
        curr = self.head # Start at First Node
        while curr: #Traverse
            print(curr.data, end=" | ") #Acess data
            curr = curr.pointer #Move to next node
        
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.AddEnd(1)
    linked_list.AddEnd(2)
    linked_list.AddEnd(3)
    linked_list.Show()