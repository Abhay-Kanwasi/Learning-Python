# SET
"""
Set are like lists, with an exception that they do not contain duplicate elements/entries.

variable = set() 
variable = {<value>} # {20}
variable = {<str>, <int>}  # {'Abhay', 5}

Set is an unordered collection. Hence order of inserting is not same as the order of access. 

set() function can be used to convert a string, list, or tuple into the set.

Sets are mutable there contents can be changed

If we want a immutable set, we use frozenset

A set cannot contain a set embedded in it.

Two sets cannot be added to create a third set.

# Accessing Set Elements
- Unordered collection, items in set cannot be accessed using incdices.
- Set cannot be sliced using []
- Entire set can be printed by just using the name of the set. 
- Iterated over using a loop

# Operations
- Built-in functions and common set operations are shown below
s = {1, 2, 4, 5, 3}
in = 12 in s
not in = 12 not in s
len = len(s)
max = max(s)
min = min(s)
sorted = sorted(s)
sum = sum(s)

# Methods
s = {1, 2, 4, 5, 3}
t = {'A', 'B', 'C'}

s.update(t) # adds elements of t to s
s.add('He') # adds 'He' to s
s.remove(<value>) # delete value from s
s.discard(<value>) # remove <value> would raised error discard won't 
s.clear() # remove all elements

# Set to check relationships between them.
s = {1, 2, 4, 5, 3}
t = {1, 3}

s.isuperset(t) # True
s.isubset(t) # False
s.isdisjoint(t) # False

"""

lst = [1, 3, 5, 6]
tpl = ('Sanjana', 23, 2.2)
s = 'Ocean'
s1 = set(lst)
s2 = set(tpl)
s3 = set(s)
# print(f"s1={s1}\ns2={s2}\ns3={s3}\n")


# Mathematical Operations

# sets
engineers = {'Ravi', 'Ram', 'Shaam', 'Abhay'}
managers = {'Ram', 'Ramesh'}

# union
print(engineers | managers)

# intersection
print(engineers & managers)

# difference
print(engineers - managers)

# symmetric difference
print(managers ^ engineers)
