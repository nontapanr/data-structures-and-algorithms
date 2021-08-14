class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size_ = 0

    def append(self, item):
        self.size_ += 1

        if self.isEmpty():
            self.head = Node(item)
            return

        current= self.head 
        newNode = Node(item)

        if item < current.data:
            newNode.next = current
            self.head = newNode
            return
            
        while(current.next != None):
            if item < current.next.data:
                newNode.next = current.next
                current.next = newNode
                return

            current = current.next
        current.next = newNode

    def isEmpty(self):
        return self.head == None

    def remove(self):
        newNode = self.head
        self.head = self.head.next
        self.size_ -= 1
        return newNode.data

    def size(self):
        return self.size_

    def __str__(self):
        current = self.head
        string = str(self.head.data)
        
        while current.next != None:
            string += " -> " + str(current.next.data)
            current = current.next

        return string


class Queue:
    def __init__(self, data = None):
        self.queue = []
        if data != None:
            for value in data:
                self.enQueue(int(value))

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        return self.queue.pop(0) if self.size() != 0 else 'Empty'

    def item(self):
        return self.queue

    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size() == 0

    def __str__(self):
        return ' '.join(str(x) for x in self.queue)


def radix_sort(L):
    q = Queue(L)
    max_bits = get_max_bits(max(L))
    qq = list(LinkedList() for i in range(10))

    for i in range (1, max_bits + 2):
        print("------------------------------------------------------------")
        print(f"Round : {i}")
        
        while not q.isEmpty():
            num = q.deQueue()
            num_digit = get_digit(num, i)
            qq[num_digit].append(num)
        check = qq[0].size()

        for a in range(10):
            print(a, ':', end = ' ')
            while not qq[a].isEmpty():
                enq = qq[a].remove()
                print(enq, end = ' ')
                q.enQueue(enq)
            print()

        if check == q.size():
            return i - 1, q

    return max_bits, q

def get_digit(n, d):
    n = abs(n)
    for i in range(d - 1):
        n //= 10
    return n % 10

def get_max_bits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


if __name__ == '__main__':
    inp = [int(x) for x in input("Enter Input : ").split()]
    times, radix = radix_sort(inp.copy())

    print("------------------------------------------------------------\n", times, ' Time(s)', sep = "")
    print("Before Radix Sort :", " -> ".join(str(x) for x in inp))
    print("After  Radix Sort :", " -> ".join(str(x) for x in radix.item()))