# High Order Function

# Q. Write a program to create a new list by obtaining square of all numbers in a list.

lst1 = [2, 3, 4, 5]

# resg = (lambda x: x ** 2)(2)
# resg = (lambda items: [n ** 2 for n in items])(lst1)
# print(resg)

new_lst = list(map(lambda n: n ** 2, lst1))
print(f"new_lst {new_lst}")


# Q. Filter out only even numbers

numbers = [2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, lst1))
print(f'even_numbers {even_numbers}')


# Q. Multiply all the numbers
from functools import reduce

numbers = [2, 3, 4, 5, 6]

product = reduce(lambda x, y: x * y, numbers)
print(f'product {product}')

# select max(salary) from employees where grade = 'skilled'

# reduce(max, map(get_salary, filter(lambda x: x.grade() == 'skilled', employees))) 
