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
    
    def countLessEqual(self, node,data):
        if node == None:
            return 0
        n = self.countLessEqual(node.left, data)
        if node.data > data:
            return n
        n += self.countLessEqual(node.right, data)
        if node.data <= data:
            n += 1
        return n

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    

if __name__ == "__main__":
    T = BST()
    inp, k = input("Enter Input : ").split("/")
    inp = [int(i) for i in inp.split()]
    
    for item in inp:
        root = T.insert(item)

    T.printTree(root)

    print("--------------------------------------------------")
    print(T.countLessEqual(root, int(k)))