# Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
# Output: [11, 12, 22, 25, 64]