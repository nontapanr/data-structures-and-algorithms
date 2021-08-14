class Stack:
    def __init__(self, lis=None):
        if lis == None:
            self.items = []
        else:
            self.items = lis

    def push(self, ch):
        self.items.append(ch)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        s = ""
        for ch in self.items:
            s += str(ch) + ""
        return s

### Functions ###
def check(openParen, closeParen):
    opens = "([{"
    closes = ")]}"
    return opens.index(openParen) == closes.index(closeParen)

def matching(data):
    errorCount = 0
    s1 = Stack()

    for i in data:
        if i in "([{":
            s1.push(i)
        else:
            if s1.isEmpty() == False:
                if check(s1.top(), i):
                    s1.pop()
                else:
                    errorCount += 1
            else:
                errorCount += 1

    return s1.size() + errorCount


##### Main #####
data = input("Enter Input : ")

error = matching(data)

if error > 0:
    print(error)
else:
    print("0\nPerfect ! ! !")


"""
testcase: ()[] -> 0
                  Perfect ! ! !
          [](] -> 2
"""
