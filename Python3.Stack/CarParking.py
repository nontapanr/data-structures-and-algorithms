class Stack:
    def __init__(self, carList = [], maxCar = None):
        if carList == ["0"] or []:
            self.cars = []
        else:
            self.cars = carList
        self.maxCar = maxCar
    
    def push(self, value):
        self.cars.append(value)

    def pop(self):
        return self.cars.pop()

    def peek(self):
        return self.cars[-1]
    
    def size(self):
        return len(self.cars)
    
    def isEmpty(self):
        return self.cars == []

    def isFull(self):
        return len(self.cars) == self.maxCar


### functions ###
def operations(command, carOp):
    if command == "arrive":
        return arrive(carOp)
    else:
        return depart(carOp)

def arrive(carOp):
    if not soi_A.isFull():
        if carOp not in soi_A.cars:
            soi_A.push(carOp)
            return f"car {carOp} arrive! : Add Car {carOp}"
        else:
            return f"car {carOp} already in soi"
    else:
        return f"car {carOp} cannot arrive : Soi Full"
    
def depart(carOp):
    if not soi_A.isEmpty():
        if carOp in soi_A.cars:
            while not soi_A.isEmpty():  # check carOp in A
                if soi_A.peek() == carOp: # if carOp == current car in soi_A
                    soi_A.pop()
                    break
                soi_B.push(soi_A.pop())

            while not soi_B.isEmpty():  # return soi B to A
                soi_A.push(soi_B.pop())
            return f"car {carOp} depart ! : Car {carOp} was remove"
        else:
            return f"car {carOp} cannot depart : Dont Have Car {carOp}"
    else:
        return f"car {carOp} cannot depart : Soi Empty"


### main ###    
if __name__ == "__main__":
    print("******** Parking Lot ********")
    input_ = input("Enter max of car,car in soi,operation : ").split()

    maxCar = int(input_[0])
    carList = input_[1].split(",")
    command = input_[2]
    carOp = input_[3]

    soi_A = Stack(maxCar, carList)
    soi_B = Stack()

    print(operations(command, carOp))
    print("[{}]".format(", ".join(soi_A.cars)))

"""
Testcase :
5 1,2,3,4 arrive 5 =>   car 5 arrive! : Add Car 5
                        [1, 2, 3, 4, 5]
4 1,2,3,4 arrive 5 =>   car 5 cannot arrive : Soi Full
                        [1, 2, 3, 4]
5 1,2,3,4 arrive 1 =>   car 1 already in soi
                        [1, 2, 3, 4]
5 0 depart 3    =>  car 3 cannot depart : Soi Empty
                    []
4 1,3,2 depart 1 => car 1 depart ! : Car 1 was remove
                    [3, 2]
6 2,3,5,7,8 depart 1 => car 1 cannot depart : Dont Have Car 1
                        [2, 3, 5, 7, 8]
"""