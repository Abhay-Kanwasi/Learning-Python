# Check if the given array is sorted or not

arr = [1, 2, 3, 4]

# Method 1
def is_array_sorted(arr):
    for index in range(len(arr) - 1):
        if arr[index] <= arr[index + 1]:
            pass
        else:
            return False
    return True

print(is_array_sorted(arr))


# Method 2
def is_array_sorted(arr, length=0):
    if length == len(arr) - 1:
        return True
    if arr[length] <= arr[length + 1]:
        pass
    else: 
        return False
    return is_array_sorted(arr, length + 1)


print(is_array_sorted(arr))