print(" *** Perfect Number Verification ***")
num = int(input("Enter number : "))
li = []
sumNum = 0

for i in range(1, num):
    if num%i == 0:
        li.append(i)
        sumNum += i

if num < 0:
    print("Only positive number !!!")
elif sumNum == num:
    print(num, "is a PERFECT NUMBER.")
    print("Factors :", li)
else:
    print(num, "is NOT a perfect number.")
    print("Factors :", li)