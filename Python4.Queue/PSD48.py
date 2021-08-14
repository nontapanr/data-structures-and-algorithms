class Queue:
    def __init__(self):
        self.queue = []
        self.countVIP = 0
    
    def enQueue(self, value):
        self.queue.append(value)

    def deQueue(self):
        if self.queue != []:
            return self.queue.pop(0)
        else:
            return "Empty"
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def insert(self, value, index):
        self.queue.insert(index, value)


def oparation(item):
    if item[0] == "EN":
        que.enQueue(item[1])
    elif item[0] == "ES":
        que.insert(item[1], que.countVIP)
        que.countVIP += 1
    else:
        print(que.deQueue())
        if que.countVIP > 0:
            que.countVIP -= 1


### Main ###
if __name__ == "__main__":
    input_ = input("Enter Input : ").split(",")
    
    que = Queue()
    
    for item in input_:
        tempItem = item.split()
        oparation(tempItem)