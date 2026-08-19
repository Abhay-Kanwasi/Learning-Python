# Tuples

# Tuples are typically used for handling heterogenous data.

# Declare Tuple
# tup = ()
# print(type(tup))

# tup = (10, )
# print(type(tup))

# tup = tuple([2, 4])

# tup = 1, 2, 4


# # Tuples are immutable

# # Access tuple elements
# msg = ("Handle", "Exception", "Like", "Ravi")
# print(msg[1])


"""QUESTIONS"""

# Pass a tuple to the divmod() function and obtain the quotaient and the remainder.

# result = divmod(17, 3)
# print(result)

# tup = (17, 3)
# result = divmod(*tup)
# print(result)


"""
Create a program to perform some actions:
- Pack first 10 multiples of 10 into a tuple
- Unpack the tuple into 10 variables, each holding 1 value
- Unpack the tuple such that first value gets stored in variable x, last value in y and all values in between into disposable variables _
- Unpack the tuple such that first value gets stored in variable i, last value in j and all values in between into a single disposable variables _
"""

# tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# a, b, c, d, e, f, g, h, i, j = tpl
# # print(tpl)
# x, _, _, _, _, _, _, _, _, y = tpl
# print(x, y, _)


# i, *_, j = tpl
# print(i, j, _)

"""
A list contains names of boys and girls as it's elements. Boys names are stored in tuples. Write a program to find out numer of boys and girls in the list.
"""
lst = [('Abhay',), ('Ravi',), 'Nisha', 'Simran', 'Radha']

boys = 0
girls = 0

for element in lst:
    if type(element) == tuple:
        boys+=1
    else:
        girls+=1

print(f'Boys {boys}\nGirls {girls}')


