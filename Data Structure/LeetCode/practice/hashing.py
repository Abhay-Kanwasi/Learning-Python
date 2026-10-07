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
# print(number_hash)
# Will get TLE

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

# print(number_hash) 


"""
Problem: Print how many time each value of q are present in s. 
s = "azyxyyzaaaa"
q = ["d", "a", "y", "z"]

Constraints
a) a <= s[i] <= z
"""

s = "azyxyyzaaaa"
q = ["d", "a", "y", "z"]

# Approch 1
character_hash = {}
character_list = [0] * 26 # all values will be small character and a-z we get total of 26 characters

for character in s:
    index = ord(character) - 97
    character_list[index] += 1
    character_hash[character] = 0

for character in q:
    index = ord(character) - 97
    character_hash[character] = character_list[index]
print(character_hash)

# Approch 2
character_hash = {}

for character in s:
    if character in character_hash:
        character_hash[character] += 1
    else:
        character_hash[character] = 1

result = {}
for character in q:
    result[character] = character_hash.get(character, 0)

print(result)



