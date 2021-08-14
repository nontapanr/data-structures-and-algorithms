def getMax(lst, maxNum = -99999):
    if len(lst) == 0:
        return maxNum
    else:
        num = lst.pop()
        if maxNum < num:
            maxNum = num
        return getMax(lst, maxNum)

def sorting(lst, result, length):
    if len(result) < length:
        temp = getMax(lst.copy())
        result.append(temp)
        lst.remove(temp)
        sorting(lst, result, length)
    return result
    

if __name__ == "__main__":
    lst = [int(i) for i in input("Enter your List : ").split(",")]

    length = len(lst)
    lst = sorting(lst, [], length)

    print(f"List after Sorted : {lst}")
