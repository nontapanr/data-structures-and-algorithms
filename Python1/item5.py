num = int(input("Enter Input : "))

for i in range(num + 2):
    for j in range(num + 1 - i):
        print('.', end='')
    for j in range(i+1):
        print('#', end='')
    if i == 0 or i == num+1:
        for j in range(num + 2):
            print('+', end='')
    else:
        for j in range(num+2):
            if j == 0 or j == num+1:
                print('+', end='')
            else:
                print('#', end='')
    print()

for i in range(num + 2):
    if i == 0 or i == num+1:
        for j in range(num + 2):
            print('#', end='')
    else:
        for j in range(num+2):
            if j == 0 or j == num+1:
                print('#', end='')
            else:
                print('+', end='')
    for j in range(num + 2 - i):
        print('+', end='')
    for j in range(i):
        print('.', end='')
    print()
