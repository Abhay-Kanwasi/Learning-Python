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