def insertion_sort(lst, start=0, length=None, progress=0):
    if length is None:
        length = len(lst)

    value = lst[start]

    index = insertion_index(lst, start, value)
    lst[index] = value
    progress += 1

    if progress > 1:
        if len(lst[progress:]) != 0:
            print(f"insert {value} at index {index} : {lst[:progress]} {lst[progress:]}")
        else:
            print(f"insert {value} at index {index} : {lst[:progress]}")

    if start+1 < length:
        insertion_sort(lst, start+1, length, progress) 
    
def insertion_index(lst, curr_index, value):
    if curr_index > 0 and lst[curr_index - 1] > value:
        lst[curr_index] = lst[curr_index - 1]
        return insertion_index(lst, curr_index - 1, value)
    else:
        return curr_index

        
if __name__ == "__main__":
    inp = [int(x) for x in input("Enter Input : ").split()]
    insertion_sort(inp)
    print("sorted")
    print(inp)
