"""
============
Questions
=============

Easy Problems
~~~~~~~~~~~~~~~

- Palindrome Check
- Reverse a String
- Reverse Words
- Check for Rotation
- First Non-Repeating
- Roman to Integer
- Implement Atoi
- Encrypt the String – II
- Equal Point in Brackets
- Anagram Checking
- P anagram Checking
- Validate IP Address
- Add Binary Strings


Medium Problems
~~~~~~~~~~~~~~~~

- Integer to Words
- Fizz Buzz
- Palindromic Sentence Check
- Isomorphic Strings
- Check for k-anagram
- Equal 0,1, and 2
- Find and replace in String
- Look and say Pattern
- Minimum repetitions to make Substring
- Excel Sheet – I
- Find the N-th character
- Next Palindromic Number with same digits
- Length of longest prefix suffix
- Longest K unique characters substring
- Smallest window containing all
- Longest substring without repeating characters
- Substrings of length k with k-1 distinct elements
- Count number of substrings
- Interleaved Strings
- Print Anagrams together
- Rank the permutation
- A Special Keyboard
- Sum of two large numbers

Hard Problems
~~~~~~~~~~~~~~

- Repeatedly Remove Duplicates
- Multiply Two Strings
- Search Pattern (KMP-Algorithm)
- Search Pattern (Rabin-Karp Algorithm)
- Shortest Common Supersequence
- Longest substring to form a Palindrome
- Longest Valid Parenthesis
- Longest Palindromic Subsequence
- Distinct Palindromic Substrings
- Palindrome Substring Queries
- Number of Distinct Subsequences
- Minimum Deletions for Palindrome
- Minimum Insertions for Palindrome
- Max Non-Overlapping Odd Palindrome Sum
"""

######################
# Easy Problems
######################


# Palindrome Check
# A palindrome is a word, phrase, number, or sequence that reads the same forwards and backwards.
def is_palindrome_approach1(string):
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False


def is_palindrome_approach2(string):
    string = string.lower()
    start_index = 0
    last_index = len(string) - 1

    while start_index < last_index:
        if string[start_index] == string[last_index]:
            start_index += 1
            last_index -= 1
        else:
            return False
    return True


def is_palindrome_approach3(string):
    string = string.lower()
    if len(string) % 2 == 0:
        middle_index = False
    else:
        middle_index = len(string) // 2
    for _ in range(len(string)):
        if middle_index:
            left = middle_index - 1
            right = middle_index + 1
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                return False
        else:
            left = middle_index
            right = middle_index + 1
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                return False
    return True


def is_palindrome_approach4(string):
    string = string.lower()
    middle_index = len(string) // 2

    for index in range(middle_index):
        left = string[index]
        right = string[len(string) - 1 - index]

        if left != right:
            return False
    return True


# Reverse a String


def reverse_string_approach1(string):
    return string[::-1]


def reverse_string_approach2(string):
    reverse_string = ""
    for index in range(len(string) - 1, -1, -1):
        reverse_string += string[index]
    return reverse_string


def reverse_string_approach3(string):
    reverse_string = ""
    for index in range(len(string)):
        reverse_string += string[len(string) - index - 1]
    return reverse_string


# Check for Rotation
"""
Given two strings s1 and s2 of equal length, determine whether s2 is a rotation of s1.
A string is said to be a rotation of another if it can be obtained by shifting some leading characters of the original string to its end without changing the order of characters.

Example : Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.

Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.

Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.
"""


def check_rotation_approach1(string1, string2):
    """
    For this approach calculate a formula for left rotation and right rotation then store one rotation at a time and then perform another rotation on updated string.
    Left rotation = last value of current string + all values except last of current string
    Right rotation = all values except last of current string + last value of current string
    Time Complexity: Left-Right rotation[O(n)] * Comparison with string2[O(n)] = O(n^2)
    """
    if len(string1) != len(string2):
        print("Both strings should be of same length")
        return False
    left_check_string = string1
    right_check_string = string1
    for index in range(len(string1)):
        right_result = right_check_string[1:] + right_check_string[0]
        right_check_string = right_result
        if right_check_string == string2:
            print(f"After {index + 1} right rotation {string1} will become {string2}")
            return True
        left_result = left_check_string[-1] + left_check_string[:-1]
        left_check_string = left_result
        if left_check_string == string2:
            print(f"After {index + 1} left rotation {string1} will become {string2}")
            return True
    print("Strings are not rotations of each other.")
    return False


def check_rotation_approach2(string1, string2):
    """
    If s2 is a rotation of s1, then when you concatenate s1 with itself, every possible rotation of s1 will appear as a substring inside that doubled string.
    we will not bei trying to update string1 step by step. Instead, we’re building a superstring that already contains all possible rotations of string1 as contiguous substrings.
    Time Complexity: linear time complexity relative to the length of the input strings
    """
    if len(string1) != len(string2):
        print("Both strings should be of same length")
        return False
    return True if string2 in (string1 + string1) else False


def check_rotation_using_kmp(string_one, string_two):
    """
    Check if string_two is a rotation of string_one using KMP.
    Example: 'abcde' → rotations: 'cdeab', 'deabc', etc.
    """
    from .algorithms import kmp_search

    if len(string_one) != len(string_two):
        print("Both strings must be of the same length")
        return False

    doubled_string = string_one + string_one
    return kmp_search(doubled_string, string_two)


# First Non-Repeating
"""
Given a string s of lowercase English letters, the task is to find the first non-repeating character. If there is no such character, return '$'.

Input: s = "geeforgs"
Output: 'f'
Explanation: 'f' is the first character in the string which does not repeat.

Input: s = "racecar"
Output: 'e'
Explanation: 'e' is the only character in the string which does not repeat.

Input: "aabbccc"
Output: '$'
Explanation: All the characters in the given string are repeating.
"""


def first_non_repeating_character_approach1(string):
    # Dictionary to store frequency of each character
    character_frequency = {}

    # First loop to count frequencies
    for character in string:
        character_frequency[character] = character_frequency.get(character, 0) + 1

    # Second loop to find first character with frequency 1
    for character in string:
        if character_frequency[character] == 1:
            return character

    # If no non-repeating character found
    return '$'
