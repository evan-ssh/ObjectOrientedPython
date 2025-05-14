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

    def findLCA(self, root, p, q):
        if root is None:
            return None
        
        if root.data == p or root.data == q:
            return root

        left_lca = self.findLCA(root.left, p, q)
        right_lca = self.findLCA(root.right, p, q)
        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca

def main():
    bt = BinaryTree()
    elements = [3, 5, 1, 6, 2, 0, 8, 7, 4]
    for elem in elements:
        bt.insert(elem)

    print("Binary Tree constructed.")

    p = int(input("Enter the first node value: "))
    q = int(input("Enter the second node value: "))

    lca = bt.findLCA(bt.root, p, q)
    if lca:
        print(f"Lowest Common Ancestor of {p} and {q}: {lca.data}")
    else:
        print(f"No common ancestor found for {p} and {q}.")

if __name__ == "__main__":
    main()