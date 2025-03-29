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
    
    def Reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextNode = curr.pointer
            curr.pointer = prev
            prev = curr
            curr = nextNode
        self.head = prev

if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.AddEnd(1)
    linked_list.AddEnd(2)
    linked_list.AddEnd(3)
    linked_list.Show()  

    linked_list.Reverse()
    linked_list.Show() 