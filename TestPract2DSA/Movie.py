class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode.next = node
    
    def displayNodes(self):
        movies = []
        currNode = self.head
        while currNode:
            movies.append(currNode.data)
            currNode = currNode.next
           
        return ", ".join(map(str,movies))
    
    def length(self):
        currNode = self.head
        counter = 0
        while currNode:
            counter += 1
            currNode = currNode.next
        return counter
def main():
    linkedList = LinkedList()
    linkedList.addNode("MOVIE1")
    linkedList.addNode("MOVIE2")
    linkedList.addNode("MOVIE3")
    print(linkedList.displayNodes())
    print(linkedList.length())
main()