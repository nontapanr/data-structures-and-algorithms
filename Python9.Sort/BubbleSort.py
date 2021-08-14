def bubbleSort(lst = []):
    n = len(lst)

    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                # print(f"{lst[j]}, {lst[j+1]} => {lst[j+1]}, {lst[j]}")
                temp = lst[j]
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
            
        if swapped == True and i >= n-2:
            print(f"last step : {lst} move[{temp}]")
            break
        elif swapped == False:
            print(f"last step : {lst} move[None]")
            break
        else:
            print(f"{i+1} step : {lst} move[{temp}]")

if __name__ == "__main__":
    inp = [int(i) for i in input("Enter Input : ").split()]
    bubbleSort(inp)