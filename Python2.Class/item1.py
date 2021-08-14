inp_Str = str(input("Enter String : "))
anslist = [0]

cnt = 1
for i in range(1, len(inp_Str)):
    check = i
    for j in range(i):
        if inp_Str[i] == inp_Str[j]:
            anslist.append(anslist[j])
            check = i
            break
        else:
            check = check + 1
    if check != i:
        anslist.append(cnt)
        cnt = cnt + 1
        continue

print(anslist)
