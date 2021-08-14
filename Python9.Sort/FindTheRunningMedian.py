l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here

    sorted_list = []
    count = 0
    for value in l:
        sorted_list_length = len(sorted_list)
        if sorted_list_length == 0:
            sorted_list.append(value)
        else:
            i = 0
            while(i < sorted_list_length):
                if sorted_list[i] >= value:
                    break
                i += 1
            sorted_list.insert(i, value)

        sorted_half = sorted_list_length//2
        if count % 2 == 0:
            median = sorted_list[sorted_half]
        elif count % 2 == 1:
            median = (sorted_list[sorted_half] + sorted_list[sorted_half+1]) / 2

        count += 1
        print(f"list = {l[:count]} : median = {median:.1f}")
