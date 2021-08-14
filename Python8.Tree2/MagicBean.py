class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        path = ""
        if self.root == None:
            self.root = Node(value)
        else:
            temp = self.root
            while temp != None:
                if value < temp.value:
                    path += "L"
                    if temp.left == None:
                        temp.left = Node(value)
                        break
                    else:
                        temp = temp.left
                else:
                    path += "R"
                    if temp.right == None:
                        temp.right = Node(value)
                        break
                    else:
                        temp = temp.right
        return path + "*"

if __name__ == "__main__":
    inp = [int(i) for i in input("Enter Input : ").split()]
    T = BinarySearchTree()

    for item in inp:
        print(T.add(item))