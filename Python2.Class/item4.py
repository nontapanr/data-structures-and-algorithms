lis = [int(x) for x in input("Enter Your List : ").split()]


def sum3(num):
    ans = []
    if len(num) > 2:
        for i in range(len(num)-2):
            for j in range(i + 1, len(num)-1):
                for k in range(j + 1, len(num)):
                    if num[i]+num[j]+num[k] == 0 and ([num[i], num[j], num[k]] not in ans):
                        ans.append([num[i], num[j], num[k]])
        return ans
    else:
        return "Array Input Length Must More Than 2"


print(sum3(lis))
