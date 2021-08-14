class Queue:
    def __init__(self):
        self.queue = []
        
    def enQueue(self, value):
        self.queue.append(value)
    
    def deQueue(self):
        return self.queue.pop(0) if self.size() != 0 else "Empty"

    def popLast(self):
        return self.queue.pop()

    def peekLast(self):
        return self.queue[-1]
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []


### main ###
if __name__ == "__main__":
    normal, mirror = input("Enter Input (Normal, Mirror) : ").split()
    normal, mirror = list(normal), list(mirror)

    bombMirror = Queue()
    bombNormal = Queue()
    defuseQueue = Queue()

    mirrorBoom = 0
    normalBoom = 0
    failed = 0

    for item in mirror:
        bombMirror.enQueue(item)
        if bombMirror.size() >= 3:
            if bombMirror.queue[-1] == bombMirror.queue[-2] == bombMirror.queue[-3]:
                mirrorBoom += 1
                defuseQueue.enQueue(item)

                for x in range(3):
                    bombMirror.popLast()

    for item in normal:
        bombNormal.enQueue(item)
        if bombNormal.size() >= 3:
            if bombNormal.queue[-1] == bombNormal.queue[-2] == bombNormal.queue[-3]:
                if defuseQueue.isEmpty():
                    normalBoom += 1
                    for x in range(3):
                        bombNormal.popLast()

                elif defuseQueue.peekLast() == item:
                    failed += 1
                    defuseQueue.popLast()
                    for x in range(2):
                        bombNormal.popLast()

                else:
                    bombNormal.queue.insert(-1, defuseQueue.popLast())

    print("NORMAL :")
    print(bombNormal.size())
    print(*bombNormal.queue[::-1] if not bombNormal.isEmpty() else "Empty", sep="")
    print(f"{normalBoom} Explosive(s) ! ! ! (NORMAL)")
    if failed != 0:
        print(f"Failed Interrupted {failed} Bomb(s)")

    print("------------MIRROR------------")
    print("MIRROR :"[::-1])
    print(bombMirror.size())
    print(*bombMirror.queue if not bombMirror.isEmpty() else "Empty"[::-1], sep="")
    print(f"(RORRIM) ! ! ! (s)evisolpxE {mirrorBoom}")