class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if not root:
            root = Node(value)
        else:
            if root.value == value:
                return root
            elif value > root.value:
                root.right = self.insert(root.right, value)
            else:
                root.left = self.insert(root.left, value)
        return root

    def delete(self, root, value):
        if root == None:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.right == None:
                temp = root.left
                root.left = None
                return temp
            elif root.left == None:
                temp = root.right
                root.right = None
                return temp

            temp = minValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        return root

    def search(self, root, value):
        if root == None or root.value == value:
            return True
        
        if value > root.value:
            return self.search(root.right, value)
        else:
            return self.search(root.left, value)

    def preOrder(self, root):
        if root == None:
            return None
        
        print(root.value, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def inOrder(self, root):
        if root == None:
            return None
        
        self.inOrder(root.left)
        print(root.value, end=" ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return None
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.value, end=" ")

    def breadthFirstSearch(self, root):
        queue = []
        queue.append(root)

        while queue != []:
            print(queue[0], end=" ")
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue.pop(0)

    
def printTree90(root, level=0):
    if root:
        printTree90(root.right, level + 1)
        print('     ' * level, root)
        printTree90(root.left, level + 1)

def minValueNode(root):
    current = root
    while current.left != None:
        current = current.left

    return current


if __name__ == "__main__":
    inp = input("Enter Input : ").split(",")
    tree = BST()
    root = None
    for item in inp:
        op, value = item.split()
        print(f"{op} : {value}", end="\n\n")
        if op == "i":
            root = tree.insert(root, int(value))
        elif op == "s":
            root = tree.search(root, int(value))
        else:
            root = tree.delete(root, int(value))
        printTree90(root)
        print('==============================================================')

    print("Preorder : ", end="")
    tree.preOrder(root)
    print()

    print("Inorder : ", end="")
    tree.inOrder(root)
    print()

    print("Postorder : ", end="")
    tree.postOrder(root)
    print()

    print("BreadthFS : ", end="")
    tree.breadthFirstSearch(root)