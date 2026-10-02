"""
1134. Armstrong Number

The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
Given a positive integer N, return true if and only if it is an Armstrong number.

Example 1:
Input: 153
Output: true

Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

Example 2:
Input: 123
Output: false

Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 
Note:
1 <= N <= 10^8
"""

# Approch 1
number = 153
armstrong = 0
original = number
len_of_number = len(str(number))

for number in str(number):
    armstrong = armstrong + int(number) ** len_of_number

print(True if armstrong == original else False)
    

# Approch 2
number = 153
armstrong = 0
original = number
len_of_number = len(str(number))

while number > 0:
    remainder = number % 10 
    armstrong = armstrong + remainder ** len_of_number
    number = number // 10
print(True if armstrong == original else False)