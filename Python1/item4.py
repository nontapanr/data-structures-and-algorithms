print('*** Fun with Drawing ***')

num = int(input('Enter input : '))

# Top_Part
for i in range(num):
    for j in range(num-i-1):
        print('.', end='')
    if(i != 0):
        print('*', end='')
        for j in range(i*2-1):
            print('+', end='')
    print('*', end='')
    for j in range((num*2)-(i*2)-3):
        print('.', end='')
    if i != num-1:
        print('*', end='')
    for j in range(i*2-1):
        print('+', end='')
    if(i != 0):
        print('*', end='')
    for j in range(num-i-1):
        print('.', end='')
    print()

# Bottom_Part
for i in range((num-1) * 2):
    for j in range(i+1):
        print('.', end='')
    print('*', end='')
    for j in range((num-2)*4-(i*2)+1):
        print('+', end='')
    if i != (num-1)*2-1:
        print('*', end='')
    for j in range(i+1):
        print('.', end='')
    print()
