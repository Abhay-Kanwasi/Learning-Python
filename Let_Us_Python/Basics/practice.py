def function(**var1):
    print(type(var1))
    result = var1 
    return result

a = function(a=10, b=11) # assignment of function to variable
# a() # calling the function

# types of arguments
"""
a. positional arguments
b. keyword arguments
c. variable length positonal arguments (*args)
d. variable length keyword arguments (**kwargs)
"""

# Functional Programming
"""
functions in pytohn they treated functions as first class data values
- it can be assigned to variables and then called using these variables.
- it can be passed as an argument to another function and returned from function.
- it can be built at execution time, the same way lists, tuples etc. can be

# Lambda functions
- normal functions have names, they are defined using def keyword.
- lambda functions do not have names. they defined using the lambda keyword and are built at execution time.
- commonly used for short functions that are convienent to define at the point they are called.
a lambda function can take any number of arguments but can only return only one value. 

Syntax: lambda arguments : expression (: separates the parameters to be passed to the lambda function and the function body. The result of running the function body is returned implicitly)
"""
# examples
## function that receives and argument and return it's cube
print(type((lambda x : x*x*x)(3)))


# Higher order functions

# def: it is a function that can receive other functions as arguments or return them

d = {'Oil': 230, 'Clip':150, 'Stud':175, 'Nut': 35}
# lambda  takes a dictionary items and return a value
de = sorted(d.items(), key=lambda kv: kv[1])
print(de)

# 3 higher order functions - map, filter, reduce

def func(n):
    return n * n
lst = [2,3,4]
r = map(func, lst)
print(list(r))