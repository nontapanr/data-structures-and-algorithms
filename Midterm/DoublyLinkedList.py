class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value) 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next_node
        return count

    def push_front(self, value):
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value, self.head, None)
            self.head.prev_node = newNode
            self.head = newNode
        
    def push_back(self, value):
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value, None, self.tail)
            self.tail.next_node = newNode
            self.tail = newNode
    
    def node_at(self, pos):
        if 0 <= pos < self.size():
            count = 0
            temp = self.head
            while temp != None:
                if count == pos:
                    return temp
                temp = temp.next_node
                count += 1
        else:
            print("List is empty or index out of bound")
            return None

    def index_of(self, value):
        count = 0
        temp = self.head
        while temp != None:
            if temp.value == value:
                return count
            temp = temp.next_node
            count += 1
        return -1
        
    def insert(self, pos, value):
        if pos == 0 or self.isEmpty():
            self.push_front(value)
        elif pos >= self.size():
            self.push_back(value)
        else:
            if pos < 0:
                pos = self.size() + pos
                if pos <= 0:
                    self.push_front(value)
                    return
            current = self.node_at(pos)
            prevNode = current.prev_node
            newNode = Node(value, current, prevNode)
            prevNode.next_node = newNode
            current.prev_node = newNode
    
    def pop_front(self):
        if self.isEmpty():
            print("list is empty")
            return -1 
        value = self.head.value
        nextNode = self.head.next_node
        if nextNode != None:
            nextNode.prev_node = None
            self.head.next_node = None
            self.head = nextNode
        else:
            self.head = self.tail = None
        return value

    def pop_back(self):
        if self.isEmpty():
            print("list is empty")
            return -1 
        value = self.tail.value
        prevNode = self.tail.prev_node
        if prevNode != None:
            prevNode.next_node = None
            self.tail.prev_node = None
            self.tail = prevNode        
        else:
            self.head = self.tail = None
        return value

    def pop(self, pos):
        if 0 <= pos < self.size() and not self.isEmpty():
            if pos == 0:
                return self.pop_front()
            elif pos == self.size()-1:
                return self.pop_back()
            else:
                current = self.node_at(pos)
                prevNode = current.prev_node
                nextNode = current.next_node
                value = current.value
                prevNode.next_node = nextNode
                nextNode.prev_node = prevNode
                current.next_node = None
                current.prev_node = None
                return value
        else:
            print("List is empty or Index out of lenght")
            print -1
    
    def add(self, value):
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            count = 0
            temp = self.head
            while temp != None:
                if temp.value <= value:
                    self.insert(count, value)
                    return
                count += 1
                temp = temp.next_node
            self.push_back(value)
    
    def compare(self, other):
        if self.size() != other.size():
            return False
        list1 = LinkedList()
        list2 = LinkedList()
        for i in range(self.size()):
            list1.add(self.node_at(i).value)
            list2.add(other.node_at(i).value)
        print(list1, list2)
        for i in range(list1.size()):
            if list1.node_at(i).value != list2.node_at(i).value:
                return False
        return True

    def __str__(self):
        if not self.isEmpty():
            temp = self.head
            outStr = ""
            while temp != None:
                outStr += str(temp.value) + " "
                temp = temp.next_node
            return outStr        
        else:
            return "empty"
    
