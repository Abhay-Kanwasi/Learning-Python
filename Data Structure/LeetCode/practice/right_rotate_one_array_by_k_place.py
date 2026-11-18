# Right rotate one array by k place

# Brute force 
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(0,k):
        temp = nums.pop()
        nums.insert(0, temp)
    return nums
print(rotate([1,2], k=3))


# little optimized version
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    rotation = k % n 
    # Rotating by k is equivalent to rotating by k % n.
    # If k is a multiple of n (k = n, 2n, 0, ...), k % n == 0,
    # so the array is unchanged and the loop does nothing.
    for _ in range(0,rotation):
        temp = nums.pop() # O(1)
        nums.insert(0, temp) # O(n)
    return nums
print(rotate([1,2], k=3))

# Time Complexity: O(r * n) # r: number of rotations, n: len of array


# Better Solution
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums[:] = nums[n-k:] + nums[:n-k] # O(k) + O(n-k) 

# Time Complexity: => O(k + n -k) => O(n)
# Space Complexity: O(1)