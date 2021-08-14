def bi_search(left, right, arr, key):
    # Code Here
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] < key:
            return bi_search(mid + 1, right, arr, key)
        elif arr[mid] > key:
            return bi_search(left, mid - 1, arr, key)
        else:
            return True
    return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))