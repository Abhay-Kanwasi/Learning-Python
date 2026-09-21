"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""

# Approch 1
words = ["cat","bt","tree","hat"] 
chars = "atach"

# words = ["hello","world","leetcode"] 
# chars = "welldonehoneyr"

total = 0
frequency_of_chars = {}
for character in chars:
    if character in frequency_of_chars:
        frequency_of_chars[character] += 1
    else:
        frequency_of_chars[character] = 1

for word in words:
    frequency_of_chars_in_words = {}
    for character in word:
        if character in frequency_of_chars_in_words:
            frequency_of_chars_in_words[character] += 1
        else:
            frequency_of_chars_in_words[character] = 1

    can_form = True
    for character in frequency_of_chars_in_words: 
        # Here it is just comparing each value of frequency_of_chars_in_words and frequency_of_chars like all items will be compared this if condition only will be executed if frequency_of_chars_in_words character count is greater then frequency_of_chars which will indicate that this word can't be formed from chars. In that case no need to count  
        if frequency_of_chars_in_words[character] > frequency_of_chars.get(character, 0):
            can_form = False 
            break

    if can_form:
        total += len(word)

print(total)
    
        