'''
 * กลุ่มที่  : 20010101
 * 62010452 นนทกร จิตรชิรานันท์
 * chapter : 7	item : 2	ครั้งที่ : 0001
 * Assigned : Saturday 17th of October 2020 02:13:16 PM --> Submission : Sunday 18th of October 2020 11:53:48 AM	
 * Elapsed time : 1300 minutes.
 * filename : 2.py
'''

"""
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()

"""
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)


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
        # Code Here
        if self.root == None:
            self.root = Node(data)
            return self.root
        p = self.root
        filled = False
        while not filled:
            if p.data > data:
                if p.left == None:
                    p.left = Node(data)
                    filled = True
                else:
                    p = p.left
            else:
                if p.right == None:
                    p.right = Node(data)
                    filled = True
                else:
                    p = p.right
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

lst = []


def inorderUntil(node, n):
    global lst
    if node != None:
        inorderUntil(node.left, n)
        if node.data >= n:
            return
        lst.append(str(node.data))
        inorderUntil(node.right, n)


T = BST()
inp1, inp2 = input('Enter Input : ').split('|')
inp1 = [int(i) for i in inp1.split()]
inp2 = int(inp2)
for i in inp1:
    root = T.insert(i)
T.printTree(root)

inorderUntil(root, inp2)

print('--------------------------------------------------')
print(f'Below {inp2} : { "Not have" if lst == [] else " ".join(lst) }')
# print(lst)


"""
Enter Input : 10 4 20 1 5|1
      20
 10
           5
      4
           1
--------------------------------------------------
Below 1 : Not have


Enter Input : 4 10 2 1 3 7 -1 -4 9|5
      10
                9
           7
 4
           3
      2
           1
                -1
                     -4
--------------------------------------------------
Below 5 : -4 -1 1 2 3 4 

Enter Input : 1 2 3 4 5 6 7 9 8 0 -1 -2|4
                                    9
                                         8
                               7
                          6
                     5
                4
           3
      2
 1
      0
           -1
                -2
--------------------------------------------------
Below 4 : -2 -1 0 1 2 3 


Enter Input : 100 70 200 34 80 300|71
           300
      200
 100
           80
      70
           34
--------------------------------------------------
Below 71 : 34 70 


Enter Input : 5 3 7 2 1 4 6 8|-5
           8
      7
           6
 5
           4
      3
           2
                1
--------------------------------------------------
Below -5 : Not have

"""