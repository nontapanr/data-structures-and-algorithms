class Queue:
    def __init__(self):
        self.queue = []

    def enQueue(self, value):
        self.queue.append(value)
    
    def deQueue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []
    
    def index(self, value):
        return self.queue.index(value)
    
    
if __name__ == "__main__":
    input_ = input("Enter Input : ").split(",")

    que = Queue()

    for item in input_:
        tempItem = item.split()
        if tempItem[0] == "E":
            que.enQueue(tempItem[1])
            print(que.size())
        else:
            if not que.isEmpty():
                dequeValue = que.queue[0]
                print(f"{dequeValue} {que.index(dequeValue)}")
                que.deQueue()
            else:
                print("-1")
    if not que.isEmpty():
        while not que.isEmpty():
            print(*que.queue)
            que.queue = []
    else:
        print("Empty")