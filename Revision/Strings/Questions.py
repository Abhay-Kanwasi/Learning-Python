# Write a python program to calculate the length of string


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