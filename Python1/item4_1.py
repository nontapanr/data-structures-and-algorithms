num = int(input("Enter : "))

col_L = 0

for i in range(num*4 - 3):

    # Left side of pyramid
    for j in range(col_L):
        if j % 2 == 0:
            print("#", end='')
        else:
            print(".", end='')
    if i < num*2-2:
        col_L = col_L + 1
    else:
        col_L = col_L - 1

    # Middle Top
    for j in range(num*4-3-abs(i*2)):
        if i % 2 == 0:
            print("#", end='')
        else:
            print(".", end='')

    # Right Top
    for j in range(i):
        if(i > (num*4 - 3)//2):
            break
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            print("#", end='')
        else:
            print(".", end='')

    # Right&Mid Bottom
    if(num*2-2 < i < num*3+1):
        for j in range((i-((num*4-4)//2))*2+1):
            if(i % 2 == 1):
                print(".", end='')
            else:
                print("#", end='')
        for j in range((num*4-4)-i):
            if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                print("#", end='')
            else:
                print(".", end='')

    print()  # new line


# OUTPUT

#################
#...............#
#.#############.#
#.#...........#.#
#.#.#########.#.#
#.#.#.......#.#.#
#.#.#.#####.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#.#.#.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#####.#.#.#
#.#.#.......#.#.#
#.#.#########.#.#
#.#...........#.#
#.#############.#
#...............#
#################
