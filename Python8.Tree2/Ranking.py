class Node:
    def __init__(self, data, rank=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.listSort = []

    def insert(self, root, data):
        if root == None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def getRank(self, node):
        if node != None:
            self.getRank(node.left)
            self.listSort.append(int(str(node)))
            self.getRank(node.right) 

    def getRankInStr(self):
        return self.listSort

if __name__ == "__main__":
    inp, find = input("Enter Input : ").split("/")
    inp = list(map(int, inp.split()))
    T = BST()
    root = None

    for item in inp:
        root = T.insert(root, item)

    T.printTree(root)
    print("--------------------------------------------------")
    print("Rank of", find, ": ", end="")
    T.getRank(root)
    listSorted = T.getRankInStr()
    isPrint = False
    
    if int(find) < listSorted[0]:
        print(0)
        isPrint = True
    else:
        for i in range(len(listSorted)):
            if listSorted[i] > int(find):
                print(i)
                isPrint = True
                break
    
    if not isPrint:
        print(len(listSorted))