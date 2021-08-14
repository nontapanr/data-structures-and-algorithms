class Queue:
    def __init__(self, queue = []):
        self.queue = queue

    def enQueue(self, value):
        self.queue.append(value)
    
    def deQueue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []


def checking(command):
    for op in command:
        tempOp = op.split()
        if tempOp[0] == "E":
            que.enQueue(tempOp[1])
        else:
            que.deQueue()
    
    isDuplicate = False
    
    for book in que.queue:
        if que.queue.count(book) > 1:
            isDuplicate = True
            break
        
    return "Duplicate" if isDuplicate else "NO Duplicate"


if __name__ == "__main__":
    listBooks, command = input("Enter Input : ").split("/")
    listBooks = listBooks.split()
    command = command.split(",")

    que = Queue(listBooks)
    print(checking(command))