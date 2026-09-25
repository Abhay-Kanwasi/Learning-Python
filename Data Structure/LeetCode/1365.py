"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
 

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

# Approch 1
nums = [8,1,2,2,3]
mapp = []
count = 0
for i in nums:
    for j in nums:
        print(f"i {i} : j {j}")
        if i > j:
            count += 1
    mapp.append(count)
    count = 0
print(mapp)

# Output limit excced


# Approch 2
nums = [8,1,2,2,3]
length = len(nums)
output = [0] * length
for index in range(length):
    for index_ in range(length):
        if nums[index] > nums[index_]:
            output[index] += 1
print(output)


# Approch 3 
def peakIndexInMountainArray(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) >> 1
        # Branchless update: pick lo or hi without an if/else branch
        lo, hi = (
            (mid + 1, hi) if arr[mid] < arr[mid + 1] else (lo, mid)
        )
    return lo