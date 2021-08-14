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
    
    def insert(self, data):
        newNode = Node(data)

        if self.root == None:
            self.root = newNode

        else:
            current = self.root
            while current != None:
                if data < current.data:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = newNode
                        return self.root
                else:
                    if current.right != None:
                        current = current.right
                    else:
                        current.right = newNode
                        return self.root

    def preOrder(self, root):
        if root == None:
            return None
        
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root == None:
            return None
        
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return None
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" ")
    
    def breadth(self, root):
        queue = []
        queue.append(root)

        while queue != []:
            print(queue[0].data, end=" ")
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue.pop(0)

if __name__ == "__main__":
    T = BinarySearchTree()
    inp = [int(i) for i in input("Enter Input : ").split()]

    for item in inp:
        root = T.insert(item)   

print("Preorder : ", end="")
T.preOrder(root)
print()
print("Inorder : ", end="")
T.inOrder(root)
print()
print("Postorder : ", end="")
T.postOrder(root)
print()
print("Breadth : ", end="")
T.breadth(root)