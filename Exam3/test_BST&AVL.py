class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height =1 
    
    def __str__(self):
        return str(self.value)
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root == None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

        def delete(self, root, value):
            if root == None:
                return root
            
            if value > root.value:
                root.right = self.delete(root.right, value)
            elif value < root.value:
                root.left = self.delete(root.left, value)
            else:
                if root.right == None:
                    temp = root.left
                    root.left = None  
                    return temp
                elif root.left == None:
                    temp = root.right
                    root.right = None
                    return temp
                
                temp = getMinNode(root.right)
                root.value = temp.value
                root.right = self.delete(root.right, temp.value)

class AVL:
    def __init__(self):
        self.root = None
    
    def insert(self, root, value):
        if root == None:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        #update
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        #LL
        if balance > 1 and self.getBalance(root.left) > value:
            return self.rightRotate(root)

        #RR
        if balance < -1 and self.getBalance(root.right) < value:
            return self.leftRotate(root)

        #LR
        if balance > 1 and self.getBalance(root.left) < value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        #RL
        if balance < -1 and self.getBalance(root.right) > value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root 

    def delete(self, root, value):
        if root == None:
            return root

        if value > root.value:
            root.right = self.delete(self.right, value)
        elif value < root.value:
            root.left = self.delete(self.left, value)
        else:
            if root.left == None:
                temp = root.right
                root = None 
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

            #update
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            
            balance = self.getBalance(root)

            # LL
            if balance > 1 and self.getBalance(root.left) >= 0:
                return self.rightRotate(root)

            # RR
            if balance < -1 and self.getBalane(root.right) <= 0:
                return self.leftRotate(root)

            # LR
            if balance > 1 and self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

            # RL
            if balance < -1 and self.getBalance(root.right) > 0:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
            
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

        #update
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

def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print("      " * level, node.value)
        printTree90(node.left, level + 1)

def getMin(root):
    current = root
    while current.left != None:
        current = current.left
    return current.value

def getMinNode(root):
    current = root
    while current.left != None:
        current = current.left
    return current
    
def getMax(root):
    current = root
    while current.right != None:
        current = current.right
    return current.value

def getFatherNode(root, child):
    queue = []
    queue.append(root)

    while queue != []:
        temp = queue.pop(0)
        if (temp.left and temp.left.value == child) or (temp.right and temp.right.value == child):
            return temp.value
        elif temp.left != None:
            queue.append(temp.left)
        else:
            queue.append(temp.right)

def preOrder(root):
    if root == None:
        return 
    print(root.value, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.value, end=" ")
    inOrder(root.right)

def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.value, end=" ")

def breadth(root):
    queue = []   
    queue.append(root)
    while queue != []:
        print(queue[0].value, end=" ")
        if queue[0].left != None:
            queue.append(queue[0].left)
        if queue[0].right != None:
            queue.append(queue[0].right)
        queue.pop(0)

lst = []
def inOrderBelow(root, value):
    global lst
    if root != None:
        inOrderBelow(root.left, value)
        if int(root.value) >= int(value):
            return
        lst.append(root.value)
        inOrderBelow(root.right, value)
    
if __name__ == "__main__":
    inp = [int(i) for i in input("Enter Input : ").split()]
    root = None
    tree = BST()
    
    for item in inp:
        root = tree.insert(root, item)

    printTree90(root)
    print("Min :", getMin(root))
    print("Max :", getMax(root))

    print("Preorder : ", end="")
    preOrder(root)
    print()

    print("Inorder : ", end="")
    inOrder(root)
    print()

    print("Postorder : ", end="")
    postOrder(root)
    print()

    print("Breadth : ", end="")
    breadth(root)
    print()

    inOrderBelow(root, 15)
    print(lst)

    print(getFatherNode(root, 4))