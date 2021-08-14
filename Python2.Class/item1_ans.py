def mapping(str1):
    temp = sorted(set(str1), key=str1.index)
    print(temp)
    a = list(map(temp.index, str1))
    return a


in_Str = str(input("Enter String : "))
print(mapping(in_Str))
