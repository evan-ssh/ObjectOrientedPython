import random

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next
            currNode.next = newNode

    def remove(self,value):
        count = 0
        curr = self.head 
        prev = None
        while curr:
            if curr.data == value:
                count+= 1
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            else:
                prev = curr
            curr = curr.next
        return count
    
    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements
    
def createLinkedList():
    linked_list = LinkedList()
    for _ in range(2000):
        linked_list.append(random.randint(1, 100))
    return linked_list


def main():
    linked_list = createLinkedList()
    num = int(input("Enter number to remove: "))
    count = linked_list.remove(num)
    print(f"{num} was removed from the linked list {count} times.")

if __name__ == "__main__":
    main()