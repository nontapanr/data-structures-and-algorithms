class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return ""
        current = self.head
        string = str(self.head.data)
        while current.next != None:
            string += " " + str(current.next.data)
            current = current.next
        return string
    
    def valuesReverse(self):
        if self.isEmpty():
            return ""
        current = self.tail
        string = str(self.tail.data)
        while current.previous != None:
            string += " " + str(current.previous.data)
            current = current.previous
        return string

    def append(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
            self.size += 1
            return
        node = Node(data)
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1
    
    def isEmpty(self):
        return self.size == 0


if __name__ == "__main__":
    data = input("Enter Input (L1,L2) : ").split()

    l1 = LinkedList()
    l2 = LinkedList()
    
    print("L1    : ", end = "")
    for value in data[0].split("->"):
        print(value, end = " ")
        l1.append(value)

    print("\nL2    : ", end = "")
    for value in data[1].split("->"):
        print(value, end = " ")
        l2.append(value)

    print("\nMerge :", l1, l2.valuesReverse())