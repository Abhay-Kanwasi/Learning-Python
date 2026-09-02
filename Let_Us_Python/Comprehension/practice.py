# Comprehension
"""
Compreshension offer an easy and compact way of creating lists, sets and dictionaries.

A compreshension works by looping or iterate over items and assigning them to container like list, set or dictionary.

This container cannot be tuple as tuple being immutable is unable to receive assignments.
"""

# List Comprehension
# [expression for var in sequence (optional for loop and/or if )]

import random
lst = []
for number in range(20):
    random_number = random.randint(10, 100)
    lst.append(random_number)
# print(f'lst {lst}')

# print([random.randint(10, 100) for number in range(20)])

lst = [str(random.randint(10, 100)) for number in range(20)]
print(type(lst[0]))

# convert a list of strings to a list of integers
int_list = [int(number) for number in lst]
print(int_list)
print(type(int_list[0]))

# generate a list of even numbers in the range of 10 to 30
ranged_numbers = [number for number in range(10, 30) if number % 2 == 0]
print(f'even numbers {ranged_numbers}')