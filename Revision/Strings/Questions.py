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

Example :

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

# Approch 1

def single_string_from_two_given_strings(string1, string2):
    new_string = string2[:2] + string1[-1] + ' ' + string1[:2] + string2[-1]
    return new_string


"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

Example :

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

Example :

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

Example :

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

Example :

string = 'abc'
nth = 1
output = 'ac'
"""

def remove_the_nth_element(string, n):
    character = string[n]
    return string.replace(character, '')


"""
Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

Example :

string = 'Abhay'
newly_string = 'ybhaA'
"""

def exchange_first_and_last_letter(string):
    newly_string = string[-1] + string[1:-1] + string[0]
    return newly_string


"""
Write a Python program to remove characters that have odd index values in a given string.

Example :

string = 'Abhay'
output = 'Aba'
"""

def remove_odd_index_character(string):
    new_string = ''
    for index in range(len(string)):
        if index % 2 != 0:
            pass
        else:
            new_string += string[index]
    return new_string


"""
Write a Python program to count the occurrences of each word in a given sentence.

Example : 

sentence = 'This is abhay and abhay is a good boy'
output = {'This: 1, 'is': 2, 'abhay' : 2, 'and' : 1, 'a' : 1, 'boy' : 1}
"""

def count_the_occurence_of_each_word_in_sentence(sentence):
    list_of_words = sentence.split(' ')
    occurence_of_words = {'word' : 'count'}
    for word in list_of_words: 
        if word in occurence_of_words.keys():
            occurence_of_words[word] += 1
        else:
            occurence_of_words[word] = 1
    return occurence_of_words


"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases.

Example :

input = 'ABhaY'
outptut 
Lower case : abhay
Upper case : ABHAY
"""

def give_lower_and_upper_case(string):
    lower_case = string.lower()
    upper_case = string.upper()
    return f'\nlower case : {lower_case}\nupper case : {upper_case}'


"""
Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).

Example :

Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white
"""

def give_distinct_words(words_sequence):
    list_of_words = words_sequence.split(',')
    print(list_of_words.remove())
    return ",".join(sorted(list(set(list_of_words))))


