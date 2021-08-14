'''
 * กลุ่มที่  : 20010101
 * 62010452 นนทกร จิตรชิรานันท์
 * chapter : 7	item : 3	ครั้งที่ : 0001
 * Assigned : Saturday 17th of October 2020 02:13:47 PM --> Submission : Sunday 18th of October 2020 12:08:56 PM	
 * Elapsed time : 1315 minutes.
 * filename : 3.py
'''
"""
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

โดยมีการป้อน input ดังนี้

i <int> = insert data

d <int> = delete data

หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว



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

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
count = 0
def inorderCount(node, n):
    global count
    if node != None:
        inorderCount(node.left, n)
        if node.data <= n:
            count += 1
        else:
            return
        inorderCount(node.right, n)

T = BST()
inp1, inp2 = input('Enter Input : ').split('/')
inp1 = [int(i) for i in inp1.split()]
inp2 = int(inp2)
for i in inp1:
    root = T.insert(i)
T.printTree(root)

inorderCount(root, inp2)
print('--------------------------------------------------')
print(count)


"""

Enter Input : 10 4 20 1 5/4
      20
 10
           5
      4
           1
--------------------------------------------------
2


Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100/-101
                100
           75
                62
      50
                28
           25
                13
 0
                -13
           -25
                -38
      -50
                -62
           -75
                -100
--------------------------------------------------
0




"""