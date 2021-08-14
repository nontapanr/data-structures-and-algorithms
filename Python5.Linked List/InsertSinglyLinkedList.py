class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0
        
    def __str__(self):
        if not self.isEmpty():
            current = self.head
            string = "link list : " + str(self.head.data)
            while current.next != None:
                string += "->" + str(current.next.data)
                current = current.next
            return string
        else:
            return "List is empty"
        
    def append(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size_ += 1

    def insert(self, index, data):
        current = self.head
        if 0 <= index <= self.size_:
            newNode = Node(data)
            print(f"index = {index} and data = {data}")
            if index == 0:
                newNode.next = current
                self.head = newNode
                self.size_ += 1
                return
            else:
                for x in range(index-1):
                    current = current.next
                newNode.next = current.next
                current.next = newNode
                self.size_ += 1
        else:
            print("Data cannot be added")
        
    def isEmpty(self):
        return self.size_ == 0  


if __name__ == "__main__":
    input_ = input("Enter Input : ").split(",")

    ll = LinkedList()

    if input_[0] != "":
        for value in input_[0].split():
            ll.append(value)
        print(ll)
    else:
        print("List is empty")

    for insertValue in input_[1:]:
        insertValue = insertValue.split(":")
        ll.insert(int(insertValue[0]), insertValue[1])
        print(ll)
