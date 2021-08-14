"""
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

โดยมีการป้อน input ดังนี้

i <int> = insert data

d <int> = delete data

หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว



"""

'''
 * กลุ่มที่  : 20010101
 * 62010452 นนทกร จิตรชิรานันท์
 * chapter : 7	item : 4	ครั้งที่ : 0002
 * Assigned : Saturday 17th of October 2020 06:08:04 PM --> Submission : Sunday 18th of October 2020 01:46:55 PM	
 * Elapsed time : 1178 minutes.
 * filename : 4.py
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # code here
        if self.root == None:
            self.root = Node(val)
            return self.root

        p = self.root
        filled = False
        while not filled:
            if p.data > val:
                if p.left == None:
                    p.left = Node(val)
                    filled = True
                else:
                    p = p.left
            if p.data <= val:
                if p.right == None:
                    p.right = Node(val)
                    filled = True
                else:
                    p = p.right
        return self.root
    
    def delete(self, r, data):
        # code here
        if r == None:
            return r

        # 2 if แรกยังไม่ได้ลบ แต่จะ traverse ลงไปเรื่อยๆ
        if r.data > data:
            r.left = self.delete(r.left, data)
        elif r.data < data:
            r.right = self.delete(r.right, data)
        # ทำการลบ
        else:
            # if เอาไว้เช็คว่ามีกิ่งทั้ง 2 ข้างมั้ย
            if r.left == None:
                temp = r.right
                r = None
                return temp
            elif r.right == None:
                temp = r.left
                r = None
                return temp

            # มีกิ่งทั้ง 2 ด้านต้องทำซับซ้อนขึ้นนิดนึง
            temp = minValNode(r.right)
            r.data = temp.data
            r.right = self.delete(r.right, temp.data)

        return r

found = False

def inorderSearch(root, data):
    global found
    if root != None:
        inorderSearch(root.left, data)
        if data == root.data:
            found = True
        inorderSearch(root.right, data)

def minValNode(root):
    if root == None:
        return root
    p = root
    while p.left != None:
        p = p.left

    return p


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

# Enter Input : i 3,i 5,i 2,d 3


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
# code here
for inst in data:
    ch, num = inst.split()
    if ch == 'i':
        print(f'insert {num}')
        printTree90(tree.insert(int(num)))
    else:
        print(f'delete {num}')
        inorderSearch(tree.root, int(num))
        if found:
            tree.root = tree.delete(tree.root, int(num))
            printTree90(tree.root)
            found = False
        else:
            print('Error! Not Found DATA')
            printTree90(tree.root)


"""
Enter Input : i 3,i 5,i 2,d 3
insert 3
 3
insert 5
      5
 3
insert 2
      5
 3
      2
delete 3
 5
      2


Enter Input : d 1,i 1,d 1,i 0,i 2,i 4,i 1,i 5,i 3,d 2
delete 1
Error! Not Found DATA
insert 1
 1
delete 1
insert 0
 0
insert 2
      2
 0
insert 4
           4
      2
 0
insert 1
           4
      2
           1
 0
insert 5
                5
           4
      2
           1
 0
insert 3
                5
           4
                3
      2
           1
 0
delete 2
                5
           4
      3
           1
 0


Enter Input : i 8,i 7,d 1,i 3,i 1,i 2,i 6,i 9,d 8,d 9,d 7,d 1,d 6,d 3,d 2
insert 8
 8
insert 7
 8
      7
delete 1
Error! Not Found DATA
 8
      7
insert 3
 8
      7
           3
insert 1
 8
      7
           3
                1
insert 2
 8
      7
           3
                     2
                1
insert 6
 8
      7
                6
           3
                     2
                1
insert 9
      9
 8
      7
                6
           3
                     2
                1
delete 8
 9
      7
                6
           3
                     2
                1
delete 9
 7
           6
      3
                2
           1
delete 7
      6
 3
           2
      1
delete 1
      6
 3
      2
delete 6
 3
      2
delete 3
 2
delete 2




"""