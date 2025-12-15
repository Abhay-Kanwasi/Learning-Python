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
"""
A palindrome is a word, phrase, number, or sequence that reads the same forwards and backwards.
"""


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
"""Reverse a string"""


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

Input: s = "geefrrgss"
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
    """
    First, we check if the string is empty; if it is, return '$'.

    Then we iterate through each character in the string.
    For each character, we generate a new string with the first occurrence of that character removed.
    If the character still exists inside that modified string, it means it appears more than once,
    so we continue to the next character.

    If the character does not appear in the modified string, it is unique,
    and we immediately return that character.

    If the loop completes and reaches the last index, we assume that no unique character exists
    and return '$'.

    Time Complexity: O(n^2)
    Because:
    - Outer loop runs O(n) times
    - Each `string.replace()` creates a new string which costs O(n)
    - Therefore total complexity = O(n) * O(n) = O(n^2)
    """
    if not string:
        return "$"
    for index in range(len(string)):
        if index == len(string) - 1:
            if string[index] in string.replace(string[index], "", 1):
                return "$"
        if string[index] in string.replace(string[index], "", 1):
            continue
        if string[index] in string:
            return string[index]
    return None


def first_non_repeating_character_approach2(string):
    if not string:
        return "$"
    char_occurrence = {}
    for char in string:
        if char in char_occurrence:
            char_occurrence[char] += 1
        else:
            char_occurrence[char] = 1
    for char in string:
        if char_occurrence[char] == 1:
            return char
    return "$"


# Roman to Integer
"""
Given a string s representing a Roman numeral, find it's corresponding integer value.
Roman numerals are formed using the following symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000.
Numbers are typically formed by combining these symbols from left to right, adding or subtracting their values based on specific rules.

Input: s = "IX"
Output: 9
Explanation: IX is a Roman symbol which represents 10 - 1 = 9

Input: s = "XL"
Output: 40
Explanation: XL is a Roman symbol which represents 50 - 10 = 40

Input: s = "MCMIV"
Output: 1904
Explanation: M is 1000, CM is 1000 - 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904
"""


def roman_to_integer(roman):
    if roman == "I":
        return 1
    elif roman == "V":
        return 5
    elif roman == "X":
        return 10
    elif roman == "L":
        return 50
    elif roman == "C":
        return 100
    elif roman == "D":
        return 500
    elif roman == "M":
        return 1000
    else:
        roman_character_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        reverse_string = roman[::-1]
        total = 0
        prev_val = 0
        for char in reverse_string:
            value = roman_character_values[char]
            if value < prev_val:
                total -= value
            else:
                total += value
            prev_val = value
        return total


# Implement Atoi
"""
Given a string s, convert it into an integer (similar to the atoi() function) without using built-in conversion functions.

Steps:
1. Skip any leading whitespaces.
2. Check for a sign (‘+’ or ‘-’). If no sign is present, assume positive.
3. Read the digits and construct the number until a non-digit character is encountered
   or the end of the string is reached. Ignore leading zeros.
4. If no digits are found, return 0.
5. Clamp the result to the 32-bit signed integer range:
      Minimum value: -2^31      → -2147483648
      Maximum value:  2^31 - 1  → 2147483647
   If the result exceeds the bounds, return the respective limit.

Examples:
Input: s = "-123"
Output: -123

Input: s = "  -"
Output: 0

Input: s = " 1231231231311133"
Output: 2147483647

Input: s = "  -0012gfg4"
Output: -12

Input: s = "  00 12gc"
Output: 0
"""


def atoi_approch_1(string):
    # Condition 1: Skip leading whitespaces
    index = 0
    while index < len(string) and string[index] == " ":
        index += 1

    # Condition 2: Checking the positive and negative sign
    sign = 1
    if string[index] == "-":
        sign = -1
        index += 1
    elif string[index] == "+":
        sign = 1
        index += 1

    # Condition 3:  Read the digits and construct the number until a non-digit character is encountered or the end of the string is reached. Ignore leading zeros.
    output = 0
    number_found = False
    while index < len(string) and ord("0") <= ord(string[index]) <= ord("9"):
        """0 ascii value is 48 and 9 ascii value is 57"""
        number_found = True
        number = (
            ord(string[index]) - ord("0")
        )  # ascii value of string - ascii value of 0 will give us the actual value in integer
        output = output * 10 + number
        index += 1

        if output > 2147483647:
            break

    # Condition 4: If no digits are found, return 0.
    if not number_found:
        return 0

    output = output * sign

    # Condition 5: Clamp the result to the 32-bit signed integer range: Minimum value: -2^31      → -2147483648 Maximum value:  2^31 - 1  → 2147483647 If the result exceeds the bounds, return the respective limit.
    minimum_range = -2147483647
    maximum_range = 2147483647

    if output < minimum_range:
        return minimum_range
    if output > maximum_range:
        return maximum_range

    return output


def atoi_approch_2(string):
    index = 0
    sign = 1
    output = 0
    number_found = False

    while index < len(string):
        character = string[index]

        # Skip leading spaces
        if character == " " and not number_found and output == 0 and sign == 1:
            index += 1
            continue

        # Handle sign
        if (character == "-" or character == "+") and not number_found and output == 0:
            sign = -1 if character == "-" else 1
            index += 1
            continue

        # Handle digit
        if ord("0") <= ord(character) <= ord("9"):
            number_found = True
            number = ord(character) - ord("0")
            output = output * 10 + number

            # Overflow check
            if output > 2147483647:
                break

            index += 1
            continue

        # Non-digit stop iteration
        break

    if not number_found:
        return 0

    output *= sign
    minimum_range = -2147483647
    maximum_range = 2147483647

    if output < minimum_range:
        return minimum_range
    if output > maximum_range:
        return maximum_range

    return output


# Encrypt the String – II
"""
You are given a string s. Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of the number of occurrences of that letter.
Then, the string thus obtained is further encrypted by reversing it [ See the sample for more clarity ]. Print the Encrypted String.

Note: All Hexadecimal letters should be converted to Lowercase letters.

Input: s = "aaaaaaaaaaa"
Output: ba

Input: s = "abc"
Output: 1c1b1a
"""


def encrypt_the_string(string):
    storage = {}
    for character in string:
        if character in storage:
            storage[character] += 1
        else:
            storage[character] = 1
    output = "".join(
        f"{character}{hex(count)[2:]}" for character, count in storage.items()
    )
    return output[::-1]


# Equal Point in Brackets
"""
Given a string of brackets, the task is to find an index k which decides the number of opening brackets is equal to the number of closing brackets. The string must be consists of only opening and closing brackets i.e. '(' and ')'.

An equal point is an index such that the number of opening brackets before it is equal to the number of closing brackets from and after. If multiple such points exist then return the first valid index and if no such index exists then return -1.

Input: str = "(())))("
Output: 4

Input: str = "))"
Output: -1
"""


def equal_point_in_brackets_approach1(string):
    for index in range(0, len(string)):
        left_bracket_count = 0
        right_bracket_count = 0

        for l_index in range(index):
            if string[l_index] == "(":
                left_bracket_count += 1
        for r_index in range(index, len(string)):
            if string[r_index] == ")":
                right_bracket_count += 1
        if left_bracket_count == right_bracket_count:
            return index
    return -1


def equal_point_in_brackets_approach2(string):
    open_count = 0
    close_count = 0

    # count total closing brackets
    for ch in string:
        if ch == ')':
            close_count += 1

    # traverse string
    for index, ch in enumerate(string):
        if open_count == close_count:
            return index

        if ch == '(':
            open_count += 1
        else:
            close_count -= 1

    return -1


# Anagram Checking
"""
Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.

Input: s1 = “geeks”  s2 = “kseeg”
Output: true

Input: s1 = "allergy", s2 = "allergyy"
Output: false

Input: s1 = "listen", s2 = "lists"
Output: false
"""

def check_anagram_approach1(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if not len(string1) == len(string2):
        return False
    else:
        string1_character_frequency = {}
        string2_character_frequency = {}
        for character in string1:
            count = 1
            if character in string1_character_frequency:
                count += 1
                string1_character_frequency[character] = count
            else:
                string1_character_frequency[character] = count
        for character in string2:
            count = 1
            if character in string2_character_frequency:
                count += 1
                string2_character_frequency[character] = count
            else:
                string2_character_frequency[character] = count
    if string1_character_frequency == string2_character_frequency:
        return True
    else:
        return False


if __name__ == "__main__":
    ...