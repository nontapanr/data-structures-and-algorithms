class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        current = self.head
        string = ""
        count = 0
        while current != None:
            string += str(current.data) + " "
            current = current.next
            if count >= self.size:
                return "Found Loop"
            count += 1
        if string == "":
            return "Empty"
        else:
            return "->".join(string.split())

    def isEmpty(self):
        return self.size == 0
    
    
    def append(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def setNext(self, src_position, des_position):
        current_src = self.head
        for i in range(src_position):
            current_src = current_src.next

        current_des = self.head
        for i in range(des_position):
            current_des = current_des.next

        print(f"Set node.next complete!, index:value = {src_position}:{current_src.data} -> {des_position}:{current_des.data}")
        current_src.next = current_des

if __name__ == "__main__":
    inp = input("Enter input : ").split(",")

    ll = LinkedList()

    for item in inp:
        command = item.split()[0]
        if command == "A":
            value = item.split()[1]
            ll.append(value)
            print(ll)
        elif command == "S":
            firstValue, secondValue = item.split()[1].split(":")
            firstValue = int(firstValue)
            secondValue = int(secondValue)
            if ll.isEmpty():
                print("Error! {list is empty}")
            else:
                if firstValue < 0 or firstValue >= ll.size:
                    print("Error! {index not in length}:", firstValue)
                else:
                    if secondValue < 0 or secondValue >= ll.size:
                        ll.append(secondValue)
                        print("index not in length, append :", secondValue)
                    else:
                        ll.setNext(firstValue, secondValue)
    if str(ll) != "Found Loop":
        print("No Loop")
    print(ll)