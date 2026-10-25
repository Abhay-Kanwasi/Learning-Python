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