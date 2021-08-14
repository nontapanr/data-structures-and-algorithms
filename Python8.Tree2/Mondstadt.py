def find_sum(data, index, size):
    if index >= size:
        return 0
    sum = find_sum(data, 2 * index + 1, size)
    sum += find_sum(data, 2 * index + 2, size) + data[index]
    return sum

if __name__ == "__main__":
    inp = input("Enter Input : ").split("/")
    
    data = [int(i) for i in inp[0].split()]
    print(sum(data))

    for item in inp[1].split(","):
        item = item.split()
        a = find_sum(data, int(item[0]), len(data))
        b = find_sum(data, int(item[1]), len(data))

        if a > b:
            operator = ">"
        elif a < b:
            operator = "<"
        else:
            operator = "="

        print(f"{item[0]}{operator}{item[1]}")