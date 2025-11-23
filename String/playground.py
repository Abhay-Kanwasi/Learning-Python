"""
input : 'aabbbccaa'
output : 'a2b3c2a2'
"""

# Pseudo Code
# Step 1: Iterate over input
# Step 2: taking first item and searching for the same item in input
# Step 3: If it matches the item then count += 1 if not then item = new item
# Step 4: Go on until last item

if __name__ == '__main__':
    string_input = 'aabbbccaa'
    prev = string_input[0]
    count = 1
    result = ''
    for string in string_input[1:]:
        # print(f'string: {string}')
        if string == prev:
            count += 1
        else:
            result += prev + str(count)
            prev = string
            count = 1
    result += prev + str(count)
    # print(result)

# Iteration 1: result="", count=1
# Iteration 2: result="", count=2
# Iteration 3: result="a2", count=1
# Iteration 4: result="a2", count=2
# Iteration 5: result="a2", count=3
# Iteration 6: result="a2b3", count=1
# Iteration 7: result="a2b3", count=2
# Iteration 8: result="a2b3c2", count=1
# Iteration 9: result="a2b3c2", count=2

# Add last character group
# result += last_character + count
# 'a2b3c2' + 'a' + 2
# 'a2b3c2a2'


"""
Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

def string_manipulation(string):
    if len(string) < 2:
        # string = 'w'
        # empty string
        return 'empty string'
    else:
        # string = 'w3resource'
        # w3ce

        # string = 'w3'
        # w3w3
        return f'{string[:2]}{string[-2:]}'

if __name__ == '__main__':
    string = 'w3resource'
    # print(string_manipulation(string))

    string = 'w3'
    # print(string_manipulation(string))

    string = 'w'
    # print(string_manipulation(string))

"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

string = 'restart'
result = ''
first_occurrence = string[0]

for i in range(1, len(string)):
    if first_occurrence == string[i]:
        result += '$'
    else:
        result += string[i]

# print(first_occurrence + result)

"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz' string1[0] = a, string1[1] = b, string1[2] = c, string2[0]=x, string2[1]=y, string2[2]=z
Expected Result : 'xyc abz'
"""
# string2[0] + string2[1] + string1[2] + " " + string1[0] + string1[1] + string2[2]
# Condition 1: single string as output from 2 given strings
# Condition 2: output will be containing 2 string which will be separated by space
# Condition 3: Swap first 2 character of each string.

# It means string1 = 'abc' and string 2 = 'xyz' then output will be 'xyc abz'

input_string1 = 'abc'
input_string2 = 'xyz'

output_string = f'{input_string2[:2]}{input_string1[-1]}' + " " + f"{input_string1[:2]}{input_string2[-1]}"
# print(output_string)

string1 = 'abc'
string2 = 'xyz'
# print(string2[0] + string2[1] + string1[2] + " " + string1[0] + string1[1] + string2[2])


"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def string_extension(string_):
    if string_[-3:] == 'ing':
            return string_ + 'ly'
    elif len(string_) >= 3:
        return string_ + 'ing'
    else:
        return string_

# print(string_extension('abc'))
# print(string_extension('string'))
# print(string_extension('ab'))

"""
Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

def contains_duplicate_approach1(nums):
    if len(nums) == len(set(nums)):
        return False
    else:

        return True

def contains_duplicate_approach2(nums):
    nums.sort()
    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1]:
            return True
    return False

"""
Valid Anagram

Given two strings string1 and string2, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

def is_anagram_approach1(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)

def is_anagram_approach2(string1, string2):
    if len(string1) != len(string2):
        return False
    list1 = []
    list2 = []
    for index in range(len(string1)):
        list1.append(ord(string1[index]))
        list2.append(ord(string2[index]))
    list1.sort()
    list2.sort()
    return list1 == list2


