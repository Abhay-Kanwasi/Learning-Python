# Print 4 time using recursion

# Tail Recurssion
def example(count = 0):
    if count == 4:
        return
    print('Tail Recurssion')
    example(count + 1)

example()


# Head Recurssion
def example(count = 0):
    if count == 4:
        return
    example(count + 1)
    print('Head Recurssion')

example()


# Print x, n times
def func(x, n):
    if n == 0:
        return 
    # print(x)
    func(2, n - 1)

func(2, 4)


# Print 1 to n using tail recursion
def example(i, n):
    if i > n:
        return
    # print(i) 
    example(i+1, n)

example(1, 5)


# Print 1 to n using head recursion 
def example(n):
    if n == 0:
        return
    # print(n)
    example(n - 1)

example(5)


# Print sum of 1 to n values 
# def total(sum, i, n):
#     if i > n:
#         print(sum)
#         return sum
#     total(sum + i, i+1, n)


def total(sum, i, n):
    print(f'sum value {sum}: {i}')
    if i > n:
        print(sum)
        return sum
    print("coming here")
    sum += i
    return sum + total(sum, i+1, n)

# print(f'total: {total(0, 1, 4)}')


# Print factorial of a number
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

number = 5
# print(f'factorial of {number} is {factorial(number)}')


# Reverse an array using recursion
def func(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    # behind the scene of above statement
    # temp = (arr[right], arr[left])   # build tuple
    # arr[left]  = temp[0]             # unpack
    # arr[right] = temp[1]

    return func(arr, left+1, right-1)

arr = [2, 5, 1, 4, 5]
# print(func(arr, 0, 4))


# Check palindrome using recursion
def is_palindrome(string, start, end):

    if start >= end:
        return True

    if string[start] != string[end]:
        return False
    
    return is_palindrome(string, start+1, end-1)

string = "nitin"
length = len(string) - 1
print(is_palindrome(string, 0, end=length))

