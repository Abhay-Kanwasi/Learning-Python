"""
Dictionary

It is a collection of key value pairs. Unlike sequence types they are indexed by keys.
Also know as maps or associative arrays

Keys in a dictionary must be unique and immutable. So strings or tuples can be used as keys as they are immutable.

Ways to create dictionary

a = {} # a = {key : value, key : value}
b = {"A1" : "Abhay", "R1" : "Ravi"}
"""

# Accessing Dictiionary Elements
dictionary = {"A1" : "Abhay", "R1" : "Ravi"}
# print(dictionary["A1"])

# for key, value in dictionary.items():
#     print(key, value)

# for key in dictionary.keys():
#     print(key)

# for value in dictionary.values():
#     print(value)

# for key in dictionary:
#     print(key)

# Dictionary Operations
"""
Dictionary are mutable. So we can perform add/delete/modify operations on a dictionary.
"""
# dictionary["A3"] = "Anubhav" # Adding a new element
# print(dictionary)

# dictionary["A1"] = "Anshul" # Modifying an existing element
# print(dictionary)

# del dictionary["R1"] # Deleting an item
# print(dictionary)

# del dictionary
# print(dictionary)

# Membership
# print('A1' in dictionary) # True
# print('R21' in dictionary) # False

# lst = list(dictionary.keys())
# print(lst)

# lst = list(dictionary)

# dictionary.clear()
# print(dictionary)

# d1 = {"A2" : "Anshul"}
# dictionary.update(d1)
# print(d1)

##  Nested dictionary
# nested_dict = {
#     "Dict1" : {"A1" : "Abhay", "R1" : "Ravi"}, 
#     "Dict2" : {"A2" : "Anshul", "R2" : "Raman"}
# }


## Questions
# 1. Create a dictionary called students containing names and ages. Copy the dictionary into stud. Empty the students dictionary, as stud continues to hold the data.

students = {"Abhay":24, "Ages":25}
stud = students.copy()
students.clear()
print(stud)

# 2. Create a list of cricketers. Use this list to create a dictionary in which the list values become the keys of the dictionary. Set the values of all keys to 50 in the dictionary created.

lst = ["Sachin", "Sunil", "Virat", "Shubhman", "Yasashvi"]
dictionary = dict.fromkeys(lst, 50)
print(dictionary)