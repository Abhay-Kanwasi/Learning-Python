"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
 
Example 1:
Input: s = "babad"
Output: "bab"

Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# Approch 1
def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    
    # dp[i][j] represents if substring s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for length 2 palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length
    
    return s[start:start + max_length]