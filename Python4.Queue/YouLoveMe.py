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



### FUNCTIONS
def changeToChar(queue):
    lis = list()
    for item in queue:
        item = item.split(":")
        if item[0] == "0":
            ch1 = "Eat"
        elif item[0] == "1":
            ch1 = "Game"
        elif item[0] == "2":
            ch1 = "Learn"
        else:
            ch1 = "Movie"
        
        if item[1] == "0":
            ch2 = "Res."
        elif item[1] == "1":
            ch2 = "ClassR."
        elif item[1] == "2":
            ch2 = "SuperM."
        else:
            ch2 = "Home"
        lis.append(f"{ch1}:{ch2}")

    return lis

def scoreCheck(myQue, yourQue):
    score = 0
    
    for i in range(len(myQue)):
        tempMy = myQue[i].split(":")
        tempYour = yourQue[i].split(":")

        if (tempMy[0] == tempYour[0]) and (tempMy[1] == tempYour[1]):
            score += 4
        elif tempMy[0] == tempYour[0]:
            score += 1
        elif tempMy[1] == tempYour[1]:
            score += 2
        else:
            score -= 5

    if score >= 7:
        print(f"Yes! You're my love! : Score is {score}.")
    elif 7 > score > 0:
        print(f"Umm.. It's complicated relationship! : Score is {score}.")
    else:
        print(f"No! We're just friends. : Score is {score}.")


### MAIN 
if __name__ == "__main__":
    inp = input("Enter Input : ").split(",")
    myQueue = list()
    yourQueue = list()
    
    for item in inp:
        item = item.split()
        myQueue.append(item[0])
        yourQueue.append(item[1])

    print("{:<5}{} =".format("My", "Queue"), ", ".join(myQueue))
    print("{:<5}{} =".format("Your", "Queue"), ", ".join(yourQueue))

    print("{:<5}{} =".format("My", "Activity:Location"), ", ".join(changeToChar(myQueue)))
    print("{:<5}{} =".format("Your", "Activity:Location"), ", ".join(changeToChar(yourQueue)))

    scoreCheck(myQueue, yourQueue)