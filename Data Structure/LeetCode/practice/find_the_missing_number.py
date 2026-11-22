# Find the missing number
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

# Brute Force Solution
n = len(nums)

for i in range(0, n+1):
    if i in nums: # This also take O(n)
        continue
    print(i)

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Better Solution
n = len(nums)

hashmap = {}
for i in range(0, n+1):
    hashmap[i] = 0

for num in nums:
    hashmap[num] = 1

result = 0
for key, value in hashmap.items():
    if value == 0:
        result = key

print(result)

# Time Complexity: O(3n) ~ O(n)
# Space Complexity: O(n)


# Optimal Solution
sum_of_all = int(n * ((n + 1) / 2))
sum_of_nums = sum(nums)

# sum_of_nums = 0 
# for num in nums:
#     sum_of_nums += num

result = sum_of_all - sum_of_nums
print(result)

# Time Complexity: O(n)
# Space Complexity: O(1)