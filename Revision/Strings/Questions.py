# Write a python program to calculate the length of string.

# Approch 1

def length_of_string1(string):
    return len(string)


# Approch 2 

def length_of_string2(string):
    length = 0
    for alphabet in string:
        length += 1
    return length


# Write a Python program to count the number of characters (character frequency) in a string.

# Approch 1

def check_character_frequency(string):
    character_occurence = {}
    for character in string:
        if character in character_occurence:
            character_occurence[character] += 1
        else:
            character_occurence[character] = 1
    return character_occurence


# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

# Approch 1

def string_made_of_first_and_last_2(string):
    if len(string) < 2:
        return ''
    else:
        return string[0:2] + string[-2:]
    


# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

# Approch 1

def change_all_occurence_except_first(string):
    first_char = string[0]
    count = 0
    for char in string:
        if char == first_char:
            if count > 1:
                new_string = string.replace(first_char, '$')
        count += 1
    new_string = first_char + new_string[1:]
    return new_string


"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

# Approch 1

def single_string_from_two_given_strings(string1, string2):
    new_string = string2[:2] + string1[-1] + ' ' + string1[:2] + string2[-1]
    return new_string


"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

# Approch 1

def add_ing_and_ly_to_string(string):
    if len(string):
        return string
    elif string.endswith('ing'):
        new_string = string + 'ly'
    else:
        new_string = string + 'ing'
    return new_string


"""
Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!' 
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

# Approch 1

def result_string(string):
    poor_index = 0
    not_index = 0
    if 'poor' and 'not' in string:
        not_index = string.index('not')
        poor_index = string.index('poor') + len('poor') 
        print(poor_index)
        new_string = string[not_index:poor_index]
        new_string = string.replace(new_string, 'good')
        return new_string
    else:
        return string


"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one.

Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""

# Approch 1

def longest_word_and_length(list_of_words):
    def longest_word(list_of_words):
        return max(list_of_words, key=len)
    return f'Longest word : {longest_word(list_of_words)} \nLength of the longest word: {len(longest_word(list_of_words))}'

"""
Write a Python program to remove the nth index character from a nonempty string.

string = 'abc'
nth = 1
output = 'ac'
"""

def remove_the_nth_element(string, n):
    character = string[n]
    return string.replace(character, '')

print(remove_the_nth_element('abc', 1))