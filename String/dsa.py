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
- First Non Repeating
- Roman to Integer
- Implement Atoi
- Encrypt the String – II
- Equal Point in Brackets
- Anagram Checking
- Panagram Checking
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
def is_palindrome(string):
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False
