'''
 * กลุ่มที่  : 20010101
 * 62010453 นนทพันธุ์ รุจิรกาล
 * chapter : 14	item : 4	ครั้งที่ : 0001
 * Assigned : Friday 9th of October 2020 01:44:31 PM --> Submission : Friday 9th of October 2020 04:27:57 PM	
 * Elapsed time : 163 minutes.
 * filename : 0005.py
'''
class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i):
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def push_front(self, value):
        if self.isEmpty():
            self.head = self.tail = self.Node(value)
        else:
            newNode = self.Node(value, self.head)
            self.head = newNode

    def insert(self, data, pos):
        if self.isEmpty() or pos == 0:
            self.push_front(data)
        elif pos >= self.size:
            self.append(data)
        else:
            current = self.nodeAt(pos)
            prev_node = self.nodeAt(pos-1)
            newNode = self.Node(data, current)
            prev_node.next = newNode
    
    def add(self, value):
        if self.isEmpty():
            self.head = self.tail = self.Node(value)
        else:
            count = 0
            temp = self.head
            while temp != None:
                if temp.data <= value:
                    self.insert(value, count)
                    return
                count += 1
                temp = temp.next
            self.append(value)


if __name__ == "__main__":
    inputlist = [int(e) for e in input('Enter numbers : ').split()]
    l = LinkedList()

    for item in inputlist:
        l.add(item)
        print(l)

    print(l)
    # list1 = LinkedList()
    # list2 = LinkedList()
    # list.contentEquivalence(list2)