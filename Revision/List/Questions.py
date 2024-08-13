from copy import deepcopy
from copy import copy

# 1. Write a Python program to sum all the items in a list. 
print(sum([1,2,3,5]))


# 2. Write a Python program to multiply all the items in a list. 
numbers = [2,4,5,4]
multiply = 1
for i in numbers:
    multiply*=i
print(multiply)


# 3. Write a python program to get largest number in the list

number_list = [2,3,4,45,6]

# Approch 1
print(f'max number approch 1 : {max(number_list)}')

# Approch 2
max_number = number_list[0]
for number in number_list:
    if number > max_number:
        max_number = number

# print(f'max number approch 2 : {max_number}')


# 4. Write a Python program to get the smallest number from a list. 

# Approch 1
# print(f'min number approch 1 : {min(number_list)}')

# Approch 2
min_number = number_list[0]
for number in number_list:
    if number < min_number:
        min_number = number
# print(f'min number approch 2 : {min_number}')


# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

sample_list = ['abc', 'xyz', 'aba', '1221']
output_strings = []
number_of_strings_in_sample_list = len(sample_list)
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        output_strings.append(string)

# print(f'outupt string {output_strings}')


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
expected_result = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last(n):
    return n[-1]

sample = [12,3,14,5]
# print(sorted(sample_list, key=last)) 


# 7. Write a Python program to remove duplicates from a list.

# Approch 1
list1 = [9,8,3,2,1,1,8]
print(f'list without duplicates approch1', list(set(list1)))

# Approch 2
list_without_duplicates = []
for number in list1:
    if number in list_without_duplicates:
        continue
    else:
        list_without_duplicates.append(number)
print(f'list without duplicates approch2{list_without_duplicates}')

# Approch 3
import pandas as pd
df = pd.DataFrame(list1)
list_without_duplicates = df.drop_duplicates()
print(f"list without duplicates approch3 {list_without_duplicates.values.flatten().tolist()}")


# 8. Write a Python program to check if a list is empty or not.

def check_list_is_empty_or_not_1(list):
    if len(list) == 0:
        return 'List is empty'
    else:
        return 'List is not empty'
    
def check_list_is_empty_or_not_2(list):
    try:
        list[0]
        return 'List is not empty'
    except IndexError:
        return 'List is empty'
    

# 9. Write a Python program to clone or copy a list.

def clone_a_list_shallow_copy(list):
    copy_list = list.copy()
    return copy_list

def copy_a_list_deep_copy(list):
    copy_list = deepcopy(list)
    return copy_list

def copy_list(list):
    copy_list = []
    for element in list:
        copy_list.append(element)
    return copy_list

def copy_list_shallow_copy(list):
    copy_list = copy(list)
    return copy_list


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def words_that_are_longer_then(this_number):
    longer_then_this_number_list = []
    list_of_words = ['dinesh', 'abhi', 'iljam', 'jam', 'oi', 'a', 'senioritta']
    for word in list_of_words:
        if len(word) > this_number:
            longer_then_this_number_list.append(word)
    return longer_then_this_number_list


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_member_in_two_list(list1, list2):
    status = False
    for element in list1:
        for this_element in list2:
            if element == this_element:
                status = True
    if status:
        return True
    else:
        return False

# 12 . Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def specified_list_after_removing_0th_4th_5th_elements(list):
    specified_list = []
    for element in range(len(list)):
        if element != 0 and element != 4 and element != 5:
            specified_list.append(list[element])
    return specified_list

def specified_list_after_removing_0th_4th_5th_elements_using_list_comprehension(list):
    specified_list = [list[i] for i in range(len(list)) if i in [0, 4, 5]]
    return specified_list

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *

# Approch 1
print([[['*' for col in range(6) ]for col in range(4)] for row in range(3)])

# Approch 2
result = []
for _ in range(3):  # Outer loop for the number of rows (3)
    outer_list = []
    for _ in range(4):  # Inner loop for the number of columns (4)
        inner_list = ['*' for _ in range(6)]  # Innermost loop for 6 asterisks
        outer_list.append(inner_list)
    result.append(outer_list)

print(result)


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

