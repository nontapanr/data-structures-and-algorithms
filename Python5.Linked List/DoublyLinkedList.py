class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None or self.tail == None

    def append(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode            
            self.head = newNode          
        
    def insert(self, pos, item):
        if pos == 0 or self.isEmpty():
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        elif pos < 0: # pos < 0 (negative)
            index = abs(pos)
            current = self.tail
            count = 0
            while current != None and count < index:
                current = current.previous
                count += 1
            if current == None:
                self.addHead(item)
            else:
                 next_node = current.next
                 newNode = Node(item)
                 newNode.next = next_node
                 newNode.previous = current
                 current.next = newNode
                 next_node.previous = newNode
        else:
            current = self.head
            count = 0
            while current != None and count != pos:
                current = current.next
                count += 1
            prev_node = current.previous
            newNode = Node(item)
            newNode.next = current
            newNode.previous = prev_node
            prev_node.next = newNode
            current.previous = newNode
            
    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        current = self.head
        while current != None:
            if current.value == item:
                return "Found"
            current = current.next
        return "Not Found"

    def index(self, item):
        current = self.head
        count = 0
        while current != None:
            if current.value == item:
                return count
            count += 1
            current = current.next
        return -1
                
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def pop(self, pos):
        if self.isEmpty() or not (0 <= pos <= self.size() - 1):
            return "Out of Range"
        else:
            if pos == 0:
                if self.isEmpty():
                    print("List is empty")
                    return -1
                first = self.head
                self.head = self.head.next
                if self.head != None:
                    first.next = None

            elif pos == self.size() - 1:
                if self.isEmpty():
                    print("List is empty")
                    return -1
                last = self.tail
                self.tail = last.previous
                if self.tail != None:
                    self.tail.next = None
                else:
                    self.head = None
                last.previous = None

            else:
                count = 0
                current = self.head
                while current != None and count != pos:
                    count += 1
                    current = current.next
                prev_node = current.previous
                next_node = current.next
                current.previous = None
                current.next = None
                if prev_node != None:
                    prev_node.next = next_node
                    next_node.previous = prev_node
            return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())