list1 = [1, 1, 1, 2, 4, 6, 7] 
list2 = [1, 2, 3, 6, 7, 8, 9, 10]

# expected output = [1,2,3,4]

length1 = len(list1)
length2 = len(list2)
result = []
i = 0
j = 0
while i < length1 and j < length2:
    if list1[i] <= list2[j]:
        if len(result) == 0 or result[-1] != list1[i]:
            result.append(list1[i])
        i += 1
    else:
        if len(result) == 0 or result[-1] != list2[j]:
            result.append(list2[j])
        j += 1

while i < length1:
    if len(result) == 0 or result[-1] != list1[i]:
        result.append(list1[i])
    i += 1

while j < length2:
    if len(result) == 0 or result[-1] != list2[j]:
        result.append(list2[j])
    j += 1

print(result)

# Time Complexity: O(n + m)
# Space Complexity: O(1)

