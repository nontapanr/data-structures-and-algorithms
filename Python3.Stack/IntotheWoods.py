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


if __name__ == "__main__":
    _input = input("Enter Input : ").split(",")

    s = Stack()
    treesList = list()

    for item in _input:
        temp = item.split()

        if temp[0] == "A":  # if A : push to stack
            s.push(int(temp[1]))

        else:   # if B : check can see trees
            count = 0
            higher = 0
            while not s.isEmpty():
                if s.peek() > higher:
                    count += 1
                    higher = s.peek()
                    treesList.append(s.pop())
                else:
                    treesList.append(s.pop())
            while len(treesList) != 0:
                s.push(treesList.pop())

            print(count)
