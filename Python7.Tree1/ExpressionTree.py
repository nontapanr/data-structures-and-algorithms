class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preOrder(self, root):
        if root == None:
            return None
        
        print(root.data, end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return None
        if root.data in ["+","-","*","/"]:
            print("(", end="")

        self.inOrder(root.left)
        print(root.data, end="")
        self.inOrder(root.right)

        if root.data in ["+","-","*","/"]:
            print(")", end="")

    def expressionTree(self, postfix):
        stack = []

        for item in postfix:
            if item not in ["+", "-", "*", "/"]:
                newNode = Node(item)
                stack.append(newNode)

            else:
                newNode = Node(item)
                node1 = stack.pop()
                node2 = stack.pop()

                newNode.right = node1
                newNode.left = node2

                stack.append(newNode)
        self.root = stack[-1]

if __name__ == "__main__":
    postfix = input("Enter Postfix : ")
    tree = BinarySearchTree()
    tree.expressionTree(postfix)

    print("Tree :")
    tree.printTree(tree.root)

    print("--------------------------------------------------")
    print("Infix :", end=' ')
    tree.inOrder(tree.root)
    print()
    
    print("Prefix :", end=' ')
    tree.preOrder(tree.root)
    print()