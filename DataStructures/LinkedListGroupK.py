class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverseInGroups(self, k):
        self.head = self._reverseInGroups(self.head, k)

    def _reverseInGroups(self, head, k):
        current = head
        prev = None
        count = 0
        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        if current:
            head.next = self._reverseInGroups(current, k)

        return prev

if __name__ == "__main__":
    ll = LinkedList()
    elements = [1, 2, 3, 4, 5, 6, 7, 8]
    for elem in elements:
        ll.append(elem)

    print("Original Linked List:")
    ll.printList()

    k = int(input("Enter the group size (k): "))
    ll.reverseInGroups(k)

    print("Reversed Linked List in Groups of k:")
    ll.printList()