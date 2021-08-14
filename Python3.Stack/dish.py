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

#### Main ####
if __name__ == "__main__":
    dishes = input("Enter Input : ").split(",")
    s1 = Stack()
    
    for item in dishes:
        weight, frequency = map(int, item.split())

        if s1.isEmpty():
            s1.push((weight, frequency))

        elif s1.top()[0] > weight:
            s1.push((weight, frequency))

        else:
            while not s1.isEmpty() and s1.top()[0] < weight:
                print(s1.pop()[1])
            s1.push((weight, frequency))