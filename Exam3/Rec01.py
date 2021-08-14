def getMin(lst, minNum = 999999):
    if len(lst) == 0:
        return minNum
    else:
        num = lst.pop()
        if minNum > num:
            minNum = num
        return getMin(lst, minNum)

def getMax(lst, maxNum = -99999):
    if len(lst) == 0:
        return maxNum
    else:
        num = lst.pop()
        if maxNum < num:
            maxNum = num
        return getMax(lst, maxNum)

def sortAscending(lst, result, length):
    if len(result) < length:
        temp = getMin(lst.copy())
        result.append(temp)
        lst.remove(temp)
        sortAscending(lst, result, length)
    return str(result)[1:-1]

def sortDescending(lst, result, length):
    if len(result) < length:
        temp = getMax(lst.copy())
        result.append(temp)
        lst.remove(temp)
        sortDescending(lst, result, length)
    return str(result)[1:-1]


if __name__ == "__main__":
    lst = list(map(int, input("Enter Input : ").split()))

    length = len(lst)
    lstAscending = sortAscending(lst.copy(), [], length)
    lstDescending = sortDescending(lst.copy(), [], length)

    print(f"List before Sorted : {lst}")
    print(f"List after Ascending Sorted  : {lstAscending}")
    print(f"List after Descending Sorted : {lstDescending}")