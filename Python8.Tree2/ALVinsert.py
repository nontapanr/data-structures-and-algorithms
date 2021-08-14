class Node: 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
  
class AVL: 
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, root, data):
        if root == None:
            return Node(data)    
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        balance = self.getBalance(root)

        # Left Left
        if balance > 1 and data < root.left.data:
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)
        # Right Right
        if balance < -1 and data >= root.right.data:
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)
        
        # Left Right
        if balance > 1 and data >= root.left.data:
            root.left = self.leftRotate(root.left)
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)
        # Right Left
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)  


if __name__ == "__main__":
    inp = list(map(int, input("Enter Input : ").split()))
    BST = AVL()
    root = None
    for item in inp:
        print("insert :", item)
        root = BST.insert(root, item)
        BST.printTree(root)
        print("===============")