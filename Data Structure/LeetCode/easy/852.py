"""
852. Peak Index in a Mountain Array

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.
Your task is to solve it in O(log(n)) time complexity.


Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1
 

Constraints:
3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""

# Approch 1
def peakIndexInMountainArray(self, arr: list[int]) -> int:
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[mid + 1]:   # condition is TRUE → peak at mid or left
            hi = mid
        else:                          # condition is FALSE → peak to the right
            lo = mid + 1
    return lo  

# Approch 2
def peakIndexInMountainArray(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1      # peak is to the right
        else:
            hi = mid          # peak is at mid or to the left
    return lo                 # lo == hi == peak index


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