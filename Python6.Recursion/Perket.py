def perket(lst, index, n):
    if n == 0:
        return 1, 0
    s, b = perket(lst, index + 1, n // 2)
    if n % 2 == 1:
        s *= int(lst[index].split()[0]);
        b += int(lst[index].split()[1]);
    return s, b

if __name__ == "__main__":
    inp = input('Enter Input : ').split(',')
    result = None
    for i in range(1, 2 ** len(inp)):
        s, b = perket(inp, 0, i)    
        result = abs(s - b) if result == None or abs(s - b) < result else result
    print(result)