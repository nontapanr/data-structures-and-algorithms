lis = input("Enter number end with (-1) : ").split("-1")

if len(lis) < 2:
    print("Invalid INPUT !!!")

else:
    countDict = {}
    dataList = list(map(int, lis[0].split())) 

    for num in dataList:
        if num in countDict.keys():
            countDict[num] += 1
        else:
            countDict[num] = 1

    if len(dataList) != 0:
        if max(countDict.values()) > (len(dataList) // 2):
            for key in countDict.keys():
                if countDict[key] == max(countDict.values()):
                    print(key)
        else:
            print("Not found 2.")
    else: 
        print("Not found 1.")