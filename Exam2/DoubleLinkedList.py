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
            print("Error")
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
            self.push_back

if __name__ == "__main__":
    inputlist = [int(e) for e in input('Enter numbers : ').split()]
    l = LinkedList()

    for item in inputlist:
        l.add(item)

    print(l)