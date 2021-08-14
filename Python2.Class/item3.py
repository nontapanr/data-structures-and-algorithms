print("*** New Range ***")

num = [float(x) for x in input("Enter Input : ").split()]


def range(*args):
    ans = []
    if len(args) == 1:
        start = 0.0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
    while start < stop:
        ans.append(round(start, 3))
        start += step

    return tuple(ans)


if len(num) == 1:
    print(range(num[0]))
elif len(num) == 2:
    print(range(num[0], num[1]))
else:
    print(range(num[0], num[1], num[2]))
