# Right rotate one array by one place

# in place change
nums = [5, 2, 3, 6, -2, 9]
nums[:] = nums[-1:] + nums[0:5]
print(nums)

# new variable 
nums = [5, 2, 3, 6, -2, 9]
num = nums[-1:] + nums[0:5]
print(num)

# without slicing
nums = [5, 2, 3, 6, -2, 9]
n = len(nums)
temp = nums[n - 1]
for i in range(n-2, -1, -1):
    nums[i + 1] = nums[i]
nums[0] = temp

