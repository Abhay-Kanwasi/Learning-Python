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
def total(sum, i, n):
    if i > n:
        print(sum)
        return sum
    total(sum + i, i+1, n)

print(f'total: {total(0, 1, 4)}')

