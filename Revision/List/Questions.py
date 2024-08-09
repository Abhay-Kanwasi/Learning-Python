# 1. Write a Python program to sum all the items in a list. 
# print(sum([1,2,3,5]))

# 2. Write a Python program to multiply all the items in a list. 
# numbers = [2,4,5,4]
# multiply = 1
# for i in numbers:
#     multiply*=i
# print(multiply)

# 3. Write a python program to get largest number in the list

number_list = [2,3,4,45,6]

# Approch 1
print(f'max number approch 1 : {max(number_list)}')

# Approch 2
max_number = number_list[0]
for number in number_list:
    if number > max_number:
        max_number = number

print(f'max number approch 2 : {max_number}')

# 4. Write a Python program to get the smallest number from a list. 

# Approch 1
print(f'min number approch 1 : {min(number_list)}')

# Approch 2
min_number = number_list[0]
for number in number_list:
    if number < min_number:
        min_number = number
print(f'min number approch 2 : {min_number}')

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

sample_list = ['abc', 'xyz', 'aba', '1221']
output_strings = []
number_of_strings_in_sample_list = len(sample_list)
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        output_strings.append(string)

print(f'outupt string {output_strings}')