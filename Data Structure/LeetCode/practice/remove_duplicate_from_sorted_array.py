# Remove duplicate from sorted array and print number of unique values in it

nums = [1, 1, 2, 3, 4, 6, 9, 10]
# Brute force solution
n = len(nums)
freq_map = {}

for index in range(n):
    freq_map[nums[index]] = 0

index = 0
for num in freq_map:
    nums[index] = num
    index += 1

print(index)
