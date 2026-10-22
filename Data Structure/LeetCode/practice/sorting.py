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

# Ascending Sorting
nums = [5, 3, 8, 4, 2]
length = len(nums)
for i in range(length):
    for j in range(length-1):
        current = j
        next = j + 1
        if nums[current] > nums[next]:
            nums[current], nums[next] = nums[next], nums[current] 
print(f'Result of ascending sorting: {nums}')