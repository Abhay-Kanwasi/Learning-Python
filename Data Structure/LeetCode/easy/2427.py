"""
Number of Common Factors

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.


Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
 

Constraints:
1 <= a, b <= 1000
"""

def commonFactors(a: int, b: int) -> int:
    from math import gcd
    g = gcd(a, b)
    
    count = 1
    d = 2
    while d * d <= g:
        exp = 0
        while g % d == 0:
            g //= d
            exp += 1
        if exp:
            count *= (exp + 1)
        d += 1
    if g > 1:  # remaining prime factor
        count *= 2
    return count