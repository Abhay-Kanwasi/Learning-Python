"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.


Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

# Method 1
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_count = 0
    current = 0
    for num in nums:
        if num == 1:
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0
    return max_count


# Method 2
nums = [1,1,0,1,1,1]

count = 0
max_count = 0
for index in range(0, len(nums)):
    if nums[index] == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
print(max(max_count, count))


# Time Complexity: O(n)
# Space Complexity: O(1)