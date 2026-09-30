"""
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
"""


# First approch
n = int(input("Given integer: "))
output = []
for number in range(1, n+1):
    if number % 3 == 0 and number % 5 == 0:
        output.append("FizzBuzz")
    elif number % 3 == 0:
        output.append("Fizz")
    elif number % 5 == 0:
        output.append("Buzz")
    else:
        output.append(str(number))

print(f"Output: {output}")


# Second approch
"""
This created a list early like if n = 3 it means answer = [0, 0, 0] it creates list first and then just replace the values later
"""
n = int(input("Given integer: "))
answer=[0]*n 
for i in range(n):
    if (i+1)%3==0 and (i+1)%5==0:
        answer[i]="FizzBuzz"
    elif (i+1)%3==0:
        answer[i]="Fizz"
    elif (i+1)%5==0:
        answer[i]="Buzz"
    else:
        answer[i]=str(i+1)

print(f"Output: {answer}")

        

