class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.value)

class AVL_BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if not root:
            return Node(value)
        
        if value >= root.value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        
        #update
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        #LL
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)
        
        #RR
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root) 

        #LR
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
            
        #RL
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def delete(self, root, value):
        if root == None:
            return root
        
        if value > root.value:
            root.right = self.delete(root.right, value)
        elif value < root.value:
            root.left = self.delete(root.left, value)
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            
            temp = self.minValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        
        #update
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balance = self.getBalance(root)

        #LL
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        #RR
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        
        #LR
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        #RL
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
            

    def minValueNode(self, root):
        if root == None:
            return root
            
        while root.left != None:
            root = root.left
        
        return root

    
    def getHeight(self, root):
        if root == None:
            return 0
        else: 
            return root.height
        
    def getBalance(self, root):
        if root == None:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        #update
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y


def printTree90(root, level=0):
    if root:
        printTree90(root.right, level + 1)
        print("     " * level, root.value)
        printTree90(root.left, level + 1)

if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    tree = AVL_BST()
    root = 0

    for item in inp:
        print(f"insert : {item}")
        root = tree.insert(root, int(item))
        printTree90(root)
        print("=============================================")
