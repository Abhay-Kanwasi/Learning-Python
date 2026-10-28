# Find the largest element of the array

nums = [55, 32, -97, 99, 3, 67]

# largest_element = nums[0] 
largest_element = float("-inf")
for num in nums:
    largest_element = max(largest_element, num)
    # if num > largest_element:
    #     largest_element = num

print(f'Largest element in {nums} is: {largest_element}')


# Time Complexity : O(n)
# Space Complexity : O(1)
