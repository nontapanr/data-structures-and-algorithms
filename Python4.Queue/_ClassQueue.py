class Queue:
    def __init__(self):
        self.queue = []
    
    def enQueue(self, value):
        self.queue.append(value)
    
    def deQueue(self):
        return self.queue.pop(0)
    
    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0
    
if __name__ == "__main__":
    que = Queue()

    que.enQueue(5)
    que.enQueue(7)
    que.enQueue(533)

    print(que.queue)