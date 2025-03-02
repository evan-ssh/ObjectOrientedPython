class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None    

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def printList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

link_list = SinglyLinkedList()
link_list.append("3")
link_list.append("7")
link_list.append("10")
link_list.printList()