"""
Given an integer input, the objective is check whether the given integer is Positive or Negative. In order to do so we have the following method,

Method 1: Using Brute Force
Method 2: Using Nested if-else Statements
Method 3: Using ternary operator
"""

# Method 1 : Using Brute Force

number = '7'
if not isinstance(number, int) or isinstance(number, float):
    print(f'{number} must be a integer or float')
else:
    if number > 0:
        print(f'{number} is a positive number.')
    elif number < 0:
        print(f'{number} is a negative number')
    else:
        print(f'{number} is zero which is nor positive or negative')

# Method 2 : Using Nested if-else Statements

number = 'ee'
if not isinstance(number, int) or isinstance(number, float):
    print(f'{number} must be a integer or float')
else:
    if number >= 0:
        if number == 0:
            print(f'{number} is zero which is nor positive or negative')
        else:
            print(f'{number} is a positive number.')
    else:
        print(f'{number} is a negative number')


# Method 3: Using ternary operator

number = 0
if not isinstance(number, int) or isinstance(number, float):
    print(f'{number} must be a integer or float')
else:
    print(f'{number} is zero which is nor positive or negative' if number == 0 else f'{number} is a positive number.' if number > 0 else f"{number} is a negative number.")