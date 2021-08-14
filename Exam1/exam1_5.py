class MyInt:
    def __init__(self, value):
        self.value = value
    
    def __sub__(self, other):
        return self.value - int(other.value * 0.5)

    def isPrime(self):
        isPri = 1
        for i in range(2, self.value):
            if self.value % i == 0 or self.value == 1:
                isPri = 0
                break
        if isPri == 0 or self.value < 2:
            return "False"
        else:
            return "True"

    def showPrime(self):
        if self.value > 2:
            for i in range(2, self.value):
                isPri = 1
                for j in range(2, i):
                    if i % j == 0:
                        isPri = 0
                        break
                if isPri == 1:
                    print(i, end=" ")
        else:
            print("!!!A prime number is a natural number greater than 1", end="")
        print("")


    ### Main ###
print(" *** class MyInt ***")
num1, num2 = input("Enter 2 number : ").split()

num1 = int(num1)
num2 = int(num2)

a = MyInt(num1)
b = MyInt(num2)
print(num1, "is Prime :", a.isPrime())
print(num2, "is Prime :", b.isPrime())
print(f"Prime number between 2 and {num1} : ", end="")
a.showPrime()
print(f"Prime number between 2 and {num2} : ", end="")
b.showPrime()
print("{} - {} = {}".format(a.value, b.value, a-b))
