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

    def ShowList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next
def display():
    print("1. Add Data")
    print("2. Show Data")
    print("3. Exit")
def main():
    link_list = SinglyLinkedList()
    while True:
        display()
        command = int(input("Enter a command"))
        if command == 1:
            data = input("Enter your data")
            link_list.append(data)
        elif command == 2:
            link_list.ShowList()
if __name__ == "__main__":
    main()