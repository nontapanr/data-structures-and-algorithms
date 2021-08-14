class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, value):
        if not root:
            root = Node(value)
        else:
            if value == root.value:
                return root
            elif value > root.value:
                root.right = self.insert(root.right, value)
            else:
                root.left = self.insert(root.left, value)

        return root

    def getMin(self, root):
        current = root
        while current.left != None:
            current = current.left

        return current.value
            
    def getMax(self, root):
        current = root
        while current.right != None:
            current = current.right
            if current.right == None:
                return current.value
        return current.value

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    inp = [int(i) for i in input("Enter Input : ").split()]
    tree = BST()
    root = None

    for item in inp:
        root = tree.insert(root, item)
        
    tree.printTree(root)

    print("------------------------------------")
    print("Min : ", tree.getMin(root))
    print("Max : ", tree.getMax(root))