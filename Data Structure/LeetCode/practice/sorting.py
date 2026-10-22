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

# most optimized version (time complexity O(n) in average and worst is still O(n^2), space complexity O(1))
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