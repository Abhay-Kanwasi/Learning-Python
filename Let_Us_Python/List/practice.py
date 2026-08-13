# List methods

# Syntax: list.method_name()

lst = [1, 2, 3, 4, 5]
lst.append(6)  # Adds an element at the end of the list
print(lst)

lst.remove(3)  # Removes the first occurrence of the specified value
print(lst)

lst.pop()  # Removes and returns the last item in the list
print(lst)

lst.pop(0)  # Removes and returns the item at the specified index
print(lst)

lst.insert(2, 10)  # Inserts an element at the specified index <index,value>
print(lst)

lst.reverse()
print(lst)

lst.sort()  # Sorts the list in ascending order
print(lst)

lst.sort(reverse=True)  # Sorts the list in descending order
print(lst)

print(lst.count(2)) # Returns the number of occurrences of the specified value

idx = lst.index(2)  # Returns the index of the first occurrence of the specified value
print(idx)

idx = lst.index(2, 3)  # Returns the index of the first occurrence of the specified value starting from index 2
print(idx)


# value --> idx
# value --> 4, 5 
# index is for where is element not Is this the element 

print(id(lst))

# OPERATIONS ON LISTS

