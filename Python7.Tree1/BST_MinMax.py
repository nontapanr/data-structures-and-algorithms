class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        newNode = Node(data)

        if self.root == None:
            self.root = newNode
        else:
            current = self.root

            while current != None:
                if current.data > data:
                    if current.left == None:
                        current.left = newNode
                        return self.root
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = newNode
                        return self.root
                    else:
                        current = current.right

    def getMin(self):
        current = self.root
        while current != None:
            if current.left != None:
                current = current.left
            else:
                return current.data
                                
    def getMax(self):
        current = self.root
        while current != None:
            if current.right != None:
                current = current.right
            else:
                return current.data

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    inp = [int(i) for i in input("Enter Input : ").split()]
    
    for item in inp:
        root = T.insert(item)

    T.printTree(root)
    print("--------------------------------------------------")
    print("Min :", T.getMin())
    print("Max :", T.getMax())
        
