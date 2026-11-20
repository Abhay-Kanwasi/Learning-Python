"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:
Input:
nums = [0, 1, 0, 3, 12]
Output: [1,3,12,0,0]

Example 2:
Input:
nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

# Brute force solution
nums = [0, 1, 0, 3, 12]
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    temp = []
    count = 0
    for num in nums:
        if num != 0:
            temp.append(num)
        else: 
            count += 1

    for index in range(length):
        if index >= length - count:
            nums[index] = 0
        else:
            print(index)
            nums[index] = temp[index]
    return nums

print(moveZeroes(nums))

# Time Complexity: O(n + n) => O(2n) ~ O(n)
# Space Complexity: O(n)


# Optimal Solution
nums = [0, 1, 0, 3, 12]
def moveZeroes(nums: list[int]) -> None:
    if len(nums) == 1:
        return 
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i+=1

    if i == len(nums):
        return 
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j+=1
    return nums

print(moveZeroes(nums))