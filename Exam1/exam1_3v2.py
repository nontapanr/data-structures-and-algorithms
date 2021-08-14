dataInput = input("Enter number end with (-1) : ").split("-1")

dataDict = {}
countList = 0

if len(dataInput) < 2:
    print("Invalid INPUT !!!")

else:
    for item in dataInput[0]:
        if item != " ":
            if item in dataDict:
                dataDict[item] += 1
            else:
                dataDict[item] = 1
            countList += 1

    if len(dataDict) > 0:
        if max(dataDict.values()) > (countList // 2):
            # max = max(dataDict.values())
            # print(dataDict[max])

            for key in dataDict.keys():
                if dataDict[key] == max(dataDict.values()):
                    print(key)
        else:
            print("Not found 2")
        
    else:
        print("Not found 1")