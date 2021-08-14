class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)    

    def isEmpty(self):
        return self.items == []

if __name__ == "__main__":
    colorList = input("Enter Input : ").split()
    # print(colorList)
    s = Stack()

    crush = 0
    gameOver = False
    while not gameOver:
        if len(colorList) == 0: # check ending
            gameOver = True

        if s.size() > 2:
            c1, c2, c3 = s.pop(), s.pop(), s.pop()
            if c1 == c2 == c3:
                crush += 1
            else:
                s.push(c3)
                s.push(c2)
                s.push(c1)
                if len(colorList) > 0:
                    s.push(colorList.pop(0))
        else:
            if len(colorList) > 0:
                s.push(colorList.pop(0))
    print(s.size())
    if s.size() != 0:
        print("".join(s.items[::-1]))
    else:
        print("Empty")
    if crush > 1:
        print(f"Combo : {crush} ! ! !")