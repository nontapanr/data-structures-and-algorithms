class Stack:
    def __init__(self):
        self.trees = []

    def push(self, tree):
        self.trees.append(tree)
    
    def pop(self):
        return self.trees.pop()

    def peek(self):
        return self.trees[-1]
    
    def size(self):
        return len(self.trees)

    def isEmpty(self):
        return self.trees == []


### function ###
def countingTrees(opInput):
    for op in opInput:
        temp = op.split()
        tempList = list()
        if op[0] == "A":
            s.push(int(temp[1]))

        elif op[0] == "S":
            while not s.isEmpty():
                if s.peek() % 2 == 0:
                    if s.peek() > 1:
                        tempList.append(s.pop() - 1)
                    else:
                        tempList.append(s.pop())
                else:
                    tempList.append(s.pop() + 2)
            while len(tempList) != 0:
                s.push(tempList.pop())

        else:
            count = 0
            closeHigher = 0
            while not s.isEmpty():
                if s.peek() > closeHigher:
                    closeHigher = s.peek()
                    tempList.append(s.pop())
                    count += 1
                else:
                    tempList.append(s.pop())
            while len(tempList) != 0:
                s.push(tempList.pop())
            print(count)


### Main ###
if __name__ == "__main__":
    _input = input("Enter Input : ").split(",")

    s = Stack()
    countingTrees(_input)