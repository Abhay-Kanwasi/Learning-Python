# Find the second largest element of the array


# Brute force approch 1 (time complexity: O(n), space complexity: O(1))
nums = [55, 32, 97, -55, 45, 32, 88, 21]
largest_element = nums[0] 
largest_element = float("-inf")
for num in nums:
    largest_element = max(largest_element, num)    
nums.remove(largest_element)

second_largest_element = float("-inf")
for num in nums:
    second_largest_element = max(second_largest_element, num)    
print(second_largest_element)


# Brute force approch 2 (time complexity: O(n), space complexity: O(1))
nums = [55, 32, 97, -55, 45, 32, 88, 21]
for count in range(2):
    second_largest_element = float("-inf")
    for num in nums:
        second_largest_element = max(second_largest_element, num)     
    if count == 0:
        nums.remove(second_largest_element)
print(second_largest_element)


# Brute force approch 3 you can't remove elements from list (time complexity: O(n log n), space complexity: O(1))
nums = [55, 32, 97, -55, 45, 32, 88, 21]
nums.sort()
print(nums[-2])


# Brute force approch 4 in case you can't remove elements from list (time complexity: ~O(n), space complexity: O(1))
nums = [55, 32, 97, -55, 45, 32, 88, 21]
largest_element = nums[0] 
largest_element = float("-inf")
second_largest_element = float("-inf")
for num in nums:
    largest_element = max(largest_element, num)    

for num in nums:
    if num < largest_element and num > second_largest_element:
        second_largest_element = num
        
print(second_largest_element)


# Optimal Solution (time complexity: O(n), space complexity: O(1))
nums = [55, 32, 97, -55, 45, 32, 88, 21]

largest_element = 0
second_largest_element = 0
for num in nums:
    if num > largest_element:
        second_largest_element = largest_element
        largest_element = num

    elif largest_element != num and num > second_largest_element:
        second_largest_element = num

print(second_largest_element)

"""
Brute-force (remove + scan): O(n) but ~3× the work, mutates the input, and gives wrong answers on duplicates (remove only deletes one copy of the max).

Optimal (two-tracker): O(n) with 1 pass, no mutation, and correct on duplicates — best on all axes, not just Big-O.
"""
