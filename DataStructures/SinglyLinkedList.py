class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# "3" -> "7" -> "10"

node1 = Node("3")
node2 = Node("7")
node3 = Node("10")
node1.next = node2#Node1 ->Node2, "3" -> "7" 
node2.next = node3#Node2 -> Node3, "7" -> "10"

currentNode = node1
while True:
    if currentNode == None:
        break
    print(currentNode.data)
    currentNode = currentNode.next