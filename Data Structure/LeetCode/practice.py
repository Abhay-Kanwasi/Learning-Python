#######################
# EXTRACTION OF DIGIT
#######################

# Problem: Count the number of digits in integer

# Approch 1
n = 5873
count = 0

while n > 0:
    n = n // 10
    count += 1
# print(count)

# Approch 2
n = 5873
from math import log10
# print(int(log10(n) + 1))


# Problem: Print all factors of a given number

num = 20

# Approch 1 (Brute Force)
result = []
for number in range(1, num+1):
    if num % number == 0:
        result.append(number)
# print(result) 

# Approch 2 (Divisor Property)
result = []
half = num // 2
for number in range(1, half+1):
    if num % number == 0:
        result.append(number)
result.append(num)
# print(result)

# Approch 3 (Square root)
num = 36

from math import sqrt
result = []
square_root = int(sqrt(num))
for number in range(1, square_root+1):
    if num % number == 0:
        result.append(number)
        output = num // number
        if output != number:
            result.append(output)
# print(result)



###################
#   HASHING
###################

# Frequency Map or Dictionary

# Problem:  Store the frequency in dictionary

nums = [5, 6, 7, 7, 7, 8, 4, 5, 6, 6]

# Approch 1
freq_map = {}

for num in nums:
    if num in freq_map:
        freq_map[num] += 1
    else:
        freq_map[num] = 1

# print(freq_map)

# Approch 2
freq_map = {}

for num in nums:
    freq_map[num] = freq_map.get(num, 0) + 1

# print(freq_map)


"""
Problem: Print how many time each value of m are present in n. 
n = [11, 3, 2, 2, 5, 7, 10]
m = [10, 2, 2, 11, 6, 7, 8]

Constraints
a) 1 <= n[i] <= 10
b) n can have 10^8 elements
c) m can have 10^8 elements
"""

n = [11, 3, 2, 2, 5, 7, 10]
m = [10, 2, 2, 11, 6, 7, 8]

# Approch 1
number_hash = {}
for m_number in m:
    if m_number < 1 or m_number > 10:
        pass
    else:
        count = 0
        for n_number in n:
            if m_number == n_number:
                count += 1
        number_hash[m_number] = count
print(number_hash)

# Approch 2
number_hash = {}
hash_list = [0] * 11 # because as per constraints we know each value can only between 0-10 nothing bigger then that.

for number in n:
    if number < 1 or number > 10:
        pass
    else:
        hash_list[number] += 1
        number_hash[number] = 0
    

for number in m:
    if number < 1 or number > 10:
        pass
    else:
        number_hash[number] = hash_list[number]

print(number_hash) 