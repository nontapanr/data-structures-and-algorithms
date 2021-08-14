def truthTable(num, result):
    if num == 0:
        print(result)
        return
    truthTable(num-1, result + "0")
    truthTable(num-1, result + "1")

if __name__ == "__main__":
    num = int(input("Enter Number : "))
    if num == 0:
        print(0)
    elif num > 0:
        truthTable(num, "")
    else:
        print("Only Positive & Zero Number ! ! !")