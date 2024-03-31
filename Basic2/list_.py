# Write a Python program to multiply and sum all the items in a list.

# mul = 1
# for i in list:
#     mul = mul*i
# print(mul)    

# sum = 0
# for i in list:
#     sum = sum*i
# print(sum)



#  Write a Python program to get the largest number from a list. # 2 approach


# list = [2,3,4,5,6,7,8,9]

##max(list)

#list.sort()
#print(list[-1])
# maxi = 0
# for i in list:
#     if i>maxi:
#         maxi = i

# print(maxi)  

#  Write a Python program to get the smallest number from a list.
# print(min(list))

# maxi = list[0]
# for i in list:
#    if i<maxi:
#         maxi = i
# print(maxi) 



# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# list1 = ['abc', 'xyz', 'aba', '1221']
# count = len(list1)

# num = 0
# for i in list1:
#     if(i[0] == i[-1]):
#         # print(i)
#         num += 1
# print(num)



#  Write a Python program to check if a list is empty or not.


# list1 = [33]

# if len(list1) == 0:
#     print("empty")
# else:
#     print("not empty")


# if not list1:
#     print("empty")
# else:
#     print("not")


# Write a program to create a list of 5 odd integers. 
# Replace the third element with a list of 4 even integers. Flatten, sort and print list.

# a = [1,3,5,7,9]

# b = [2,4,6,8]

# a[3] = b
# print(a) # [1, 3, 5, [2, 4, 6, 8], 9]

# new = []
# for i in a:
#     if isinstance(i, list):
#         for j in i:
#             new.append(j)
#     else:
#         new.append(i)

# new2 = sorted(new)
# print(new2)


# Suppose a list has 20 numbers. Write a program that remove duplicate from this list.
# lst = [1,2,3,4,5,6,7,8,9,2,4,6,8,9,11,12,13,11,13,15]
# lst_2 =[]
# for i in lst:
#     if i not in lst_2:
#         lst_2.append(i)
# print(lst_2)
