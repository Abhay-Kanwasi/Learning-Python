# Remove duplicate from sorted array and print number of unique values in it

# Brute force solution
nums = [1, 1, 2, 3, 4, 6, 9, 10]
n = len(nums)
freq_map = {}

for index in range(n):
    freq_map[nums[index]] = 0

index = 0
for num in freq_map:
    nums[index] = num
    index += 1

print(index)

# Time complexity : O(n + n) => O(2n) ~ O(n)
# Space complexity: O(n) as in worst case the dictionary stack will be full as list if every num is unique


# Optimal solution
nums = [1, 1, 2, 3, 4, 6, 9, 10]

n = len(nums)

if n == 1: 
    print(1)

pointer_a = 0
pointer_b = pointer_a + 1

while pointer_b < n:
    if nums[pointer_b] != nums[pointer_a]:
        pointer_a += 1
        nums[pointer_a], nums[pointer_b] = nums[pointer_b], nums[pointer_a] 
    pointer_b += 1

unique_values = pointer_a  + 1
print(unique_values)

# Time complexity: O(n)
# Space complexity: O(1)