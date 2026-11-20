nums = [5, 3, 9, 8, 1, 6, 4, -10]
print(f'Nums: {nums}')
target = int(input("Target: "))

target_index = -1
for index in range(len(nums)):
    if nums[index] == target:
        target_index = index
        break

print(f'For nums\n{nums}\n{target} is present on {target_index}')

# Time Complexity : O(n)
# Space Complexity : O(1)