class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

def rightViewUtil(node, level, max_level, result):
    if node is None:
        return
    if level > max_level[0]:
        result.append(node.data)
        max_level[0] = level
    rightViewUtil(node.right, level + 1, max_level, result)
    rightViewUtil(node.left, level + 1, max_level, result)

def rightView(root):
    result = []
    max_level = [0]
    rightViewUtil(root, 1, max_level, result)
    print("Right view of the tree:", " ".join(map(str, result)))

def main():
    bt = BinaryTree()
    elements = [1, 2, 3, 5, 4, 6]
    for elem in elements:
        bt.insert(elem)
    rightView(bt.root)

if __name__ == "__main__":
    main()