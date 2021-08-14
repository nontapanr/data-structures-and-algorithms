def rotateA(str):
    firstStr = str[-2::]
    secondStr = str[:-2:]
    return firstStr + secondStr

def rotateB(str):
    firstStr = str[3::]
    secondStr = str[:3:]
    return firstStr + secondStr

#### Main ####
print("*** String Rotation ***")

num1, num2 = input("Enter 2 stirng : ").split()

count = 1
temp1 = num1
temp2 = num2

while rotateA(temp1) != num1 or rotateB(temp2) != num2:
    temp1 = rotateA(temp1)
    temp2 = rotateB(temp2)

    if count <= 5:
        print(f"{count} {temp1} {temp2}")
        
    count += 1

else: 
    if count > 5:
        print(" . . . . .")

    temp1 = rotateA(temp1)
    temp2 = rotateB(temp2)
    print(f"{count} {temp1} {temp2}")
    print(f"Total of  {count} rounds.")
