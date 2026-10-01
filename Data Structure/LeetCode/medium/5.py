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


# Approch 2
def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
    
        start = 0
        max_length = 1
        
        def expand_around_center(left: int, right: int) -> int:
            """Returns the length of palindrome expanding from center"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of palindrome (right - left - 1)
            return right - left - 1
        
        for i in range(len(s)):
            # Check for odd length palindromes (center at i)
            len1 = expand_around_center(i, i)
            
            # Check for even length palindromes (center between i and i+1)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length
            current_max = max(len1, len2)
            
            # Update if we found a longer palindrome
            if current_max > max_length:
                max_length = current_max
                # Calculate start position
                start = i - (current_max - 1) // 2
        
        return s[start:start + max_length]