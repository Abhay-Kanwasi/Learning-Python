# Count the number of digits in integer

# Approch 1
n = 5873
count = 0

while n > 0:
    n = n // 10
    count += 1
print(count)


# Approch 2
n = 5873
from math import log10
print(int(log10(n) + 1))


# Print all factors of a given number

num = 20

# Approch 1 (Brute Force)

result = []
for number in range(1, num+1):
    if num % number == 0:
        result.append(number)
print(result) 


# Approch 2 (Divisor Property)

result = []
half = num // 2
print(half)
for number in range(1, half+1):
    if num % number == 0:
        result.append(number)
result.append(num)
print(result)


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
print(result)


# Frequency Map or Dictionary

# Store the frequency in dictionary

nums = [5, 6, 7, 7, 7, 8, 4, 5, 6, 6]

# Approch 1
freq_map = {}

for num in nums:
    if num in freq_map:
        freq_map[num] += 1
    else:
        freq_map[num] = 1

print(freq_map)

# Approch 2
freq_map = {}

for num in nums:
    freq_map[num] = freq_map.get(num, 0) + 1

print(freq_map)