def binary_search(arr, search):
    sorted_array = sorted(arr)
    lower = 0
    upper = len(arr)-1
    pos = 0
    while lower <= upper:
        mid = (lower + upper)//2
        if sorted_array[mid] == search:
            return array.index(search) + 1
        else:
            if sorted_array[mid]<search:
                lower = mid
            else:
                upper = mid
    return None


array = [3,4,2,1,5]
search = int(input("Enter the number you are searching for : "))
print(f'Value found at {binary_search(array,search)}.')

