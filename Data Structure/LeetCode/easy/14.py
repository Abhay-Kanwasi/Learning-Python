"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

# Approch 1
def isValid(self, s: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in bracket_map:
            # This is a closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # This is an opening bracket
            stack.append(char)
    
    # Valid only if all brackets are matched (stack is empty)
    return len(stack) == 0