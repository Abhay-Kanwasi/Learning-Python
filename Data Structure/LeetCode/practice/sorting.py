nums = [5, 7, 8, 4, 1, 6, 9, 2]
sorted_nums = nums
min_index = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    nums.insert(i, nums.pop(min_index))

print(nums)