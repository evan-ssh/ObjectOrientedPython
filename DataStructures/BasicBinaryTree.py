class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.left is None:
            node.left = Node(value)
        elif node.right is None:
            node.right = Node(value)
        else:
            self._insert(node.left, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)

bt.inorder(bt.root)  
