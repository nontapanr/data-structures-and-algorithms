def bubble_sort(lst):
    result = lst.copy()
    for i in range(len(result) - 1):
        swapped = False
        for j in range(len(result) - i - 1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def subset_sum(targer, lst, left=0, res=[], carry=[]):
    if left >= len(lst):
        return res
    carry.append(lst[left])
    if sum(carry) == target:
        res.append(carry.copy())
    res = subset_sum(target, lst, left+1, res, carry)
    carry.pop()
    res = subset_sum(target, lst, left+1, res, carry)
    return res

def list_order(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

if __name__ == "__main__":
    inp = input("Enter Input : ").split("/")
    target = int(inp[0])
    inp_list = list(map(int, inp[1].split()))

    inp_list = bubble_sort(inp_list)
    result_list = subset_sum(target, inp_list)
    if len(result_list) == 0:
        print("No Subset")
    else:
        result_list = list_order(result_list)
        for item in result_list:
            print(item) 
