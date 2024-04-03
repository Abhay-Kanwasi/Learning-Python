""""
Tuples are immutable
Syntax: () | (10,)
"""

# A list contains tuples containing roll number, names and age of student. Write a python program to gather all the names from this list into another list.

# lst = [('OO9', 'Abhy', 1), ('O19', 'Hbhy', 2), ('19', 'Hbfhy', 3)]

# lst_2 =[]

# # iterate lst[1] 
# for i in lst:
#     lst_2.append(i[1])

# print(lst_2)


# Write a Python program to check whether an element exists within a tuple.

# tpl = ('OO9', 'Abhy', '1')
# check =  input("Enter :")
# output = 'False'
# for i in tpl:
#     if check == i:
#         output = 'True'
#     else:
#         continue  
# print(output)


# Write a Python program to convert a tuple to a string.
# tpl = ('OO9', 'Abhy', '1')
# print(type(str(tpl)))

# Write a Python program to remove an item from a tuple.
# tpl = ('OO9', 'Abhy', '1')
# print(type(list(tpl)))
# lst = list(tpl)
# lst.remove('1')
# tpl_2 = tuple(lst)
# print(tpl_2)

# Write a Python program to reverse a tuple.

# tpl = ('OO9', 'Abhy', 1)
# print(tpl[::-1])



# Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
e = []
for t in L:
    if t:
        e.append(t)
print(e)





