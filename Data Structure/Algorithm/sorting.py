# SELECTION SORT

print("SELECTION SORT")

# Ascending Sorting
nums = [5, 7, 8, 4, 1, 6, 9, 2]
for first in range(len(nums)):
    min_index = first
    for second in range(first+1, len(nums)):
        if nums[min_index] > nums[second]:
            min_index = second
    nums[first], nums[min_index] = nums[min_index], nums[first]
print(f'Result of ascending sorting: {nums}')

# Descending Sorting
nums = [5, 7, 8, 4, 1, 6, 9, 2]
for first in range(len(nums)):
    max_index = first
    for second in range(first+1, len(nums)):
        if nums[max_index] < nums[second]:
            max_index = second
    nums[first], nums[max_index] = nums[max_index], nums[first]
print(f'Result of desending sorting: {nums}')


# BUBBLE SORT

print("\nBUBBLE SORT")

# Ascending Sorting (time complexity O(n(n - 1)) means O(n^2) average and worst, space complexity O(1))
nums = [5, 3, 8, 4, 2]
length = len(nums)
for i in range(length):
    for j in range(length-1):
        current = j
        next = j + 1
        if nums[current] > nums[next]:
            nums[current], nums[next] = nums[next], nums[current] 
print(f'Result of ascending sorting: {nums}')

# optimized version (time complexity O(n(n + 1)/2) means O(n^2) average and worst, space complexity O(1))
nums = [5, 3, 8, 4, 2]
length = len(nums)
for i in range(length - 2, -1, -1): # Why Each pass puts the biggest number in its final spot on the right, so next pass we ignore that spot. `i` just marks where the unsorted part ends, and it shrinks each time.
    for j in range(0, i+1):
        current = j
        next = j + 1
        if nums[current] > nums[next]:
            nums[current], nums[next] = nums[next], nums[current] 
print(f'Result of optimized ascending sorting: {nums}')

# most optimized version (Best case O(n) (already sorted, exits after 1 pass), average and worst O(n²), space O(1))
nums = [5, 3, 8, 4, 2]
for i in range(length - 2, -1, -1):
    swapped = False
    for j in range(0, i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swapped = True
    if not swapped:          # a full pass with no swaps ⇒ sorted
        break
print(f'Result of most optimized ascending sorting: {nums}')


# INSERTION SORT

print("\nINSERTION SORT")

nums = [3, 5, 4, 9, 2]

"""
Variable	    Meaning
current_index	The position of the element we're currently inserting into the sorted portion
key	            The value being inserted (the "card" we're placing in our hand)
compare_index	Walks leftward through the sorted portion, comparing each element to key
"""

# Start from index 1 — the first element is already "sorted" (Time: O(n²) worst case (reverse-sorted), O(n) best case (already sorted) and Space: O(1) — sorts in place..

for current_index in range(1, len(nums)):
    key = nums[current_index]        # element we want to insert into the sorted portion
    compare_index = current_index - 1

    # Shift elements of nums[0..current_index-1] that are greater than key one position right
    while compare_index >= 0 and nums[compare_index] > key:
        nums[compare_index + 1] = nums[compare_index]
        compare_index -= 1

    # Place key in its correct position
    nums[compare_index + 1] = key

print(nums)   # [2, 3, 4, 5, 9]


# MERGE SORT

print("\nMERGE SORT")

nums = [3, 5, 4, 9, 2]

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr

print(mergeSort(nums, 0, len(nums) - 1))


# QUICK SORT

print("\nQUICK SORT")

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx)
        quick_sort(arr, pivot_idx + 1, high)
    
    return arr


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]   # middle element as pivot
    i, j = low - 1, high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


# Usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print(arr)  # [1, 5, 7, 8, 9, 10]