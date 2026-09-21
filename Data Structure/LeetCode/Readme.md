# Intution behind probelems

## Problem 1523
- Approch 1 is brute force O(high-low) complexity
- Approch 2 is optimized O(1) complexity

### Simple intuition behind Approch 2

Odd numbers come every 2 numbers:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
   ↑     ↑     ↑     ↑     ↑
```
So if you have numbers 0 to n, roughly half of them are odd.

But "roughly half" is not exact. Let's see:

The key observation
Write n as pairs:

```text
(0,1) (2,3) (4,5) (6,7) ...
```
Each pair has exactly one odd number.

Now:

- If n is odd → the last number completes a pair, so count = (n+1)/2

- If n is even → the last number is the start of a new pair, no odd yet, so count = n/2

We want one formula that handles both cases.

How to make one formula, Look at what we want:

```
n	count

6	3

7	4

8	4

9	5
```
Notice: when n is even, count = n/2.
When n is odd, count = (n+1)/2.

That is exactly:

```text
count = (n + 1) // 2
```
Why? Because:

- If n is even: (n+1) // 2 rounds down to n/2 
- If n is odd: (n+1) // 2 = (n+1)/2 exactly 

So why +1 before dividing?
Because we want the formula to round up when n is odd, and stay the same when n is even.

Adding 1 before dividing does exactly that:

- n even → n+1 is odd → integer division rounds down → gives n/2

- n odd → n+1 is even → divides perfectly → gives (n+1)/2

#### Why not n // 2 + 1?
Because n // 2 + 1 always adds 1, even when n is even.

Example: n = 6

```text
6 // 2 + 1 = 3 + 1 = 4  (should be 3)
```

The +1 should only happen when n is odd. Adding it before the division lets the division "absorb" it when n is even.

<b>One line answer</b>

We add 1 before dividing so that the division rounds up for odd n and stays for even n. That is exactly what counting odd numbers needs.


## Problem 389

- Approch 1 brute force approch
- Approch 2 is best approch for this scenario

### Simple intution behind Approch 3
XOR(^ it is a bitwise operator) every character of s and t together. Matching characters cancel to 0, only the extra one survives.

So we just loop through both strings and storing all in result variable so whenever it gets the same value it cancel it and the one don't have any value similar to get filter out we just need to convert it back to character using chr.

Note: When you will see it per iteration you will see numbers getting 97 to 23 or like this don't worry about them just keep in mind how xor works.

Why it works:

```text
a ^ a = 0
a ^ 0 = a
```
So s and t characters cancel, leaving the extra letter.

But python doesn't allow ^ on strings but we can avoid it by using ord and chr methods.

Let's say:

```text
s = "ab"
t = "abc"
```

Characters and ASCII:

```text
a = 97
b = 98
c = 99
```

Now trace:
text
result = 0

<b>loop over s</b>
result ^= 97   → 0 ^ 97 = 97
result ^= 98   → 97 ^ 98 = 3

<b>loop over t</b>
result ^= 97   → 3 ^ 97 = 98
result ^= 98   → 98 ^ 98 = 0
result ^= 99   → 0 ^ 99 = 99

result = 99 → chr(99) = 'c'
Look at the intermediate values: 0 → 97 → 3 → 98 → 0 → 99.

Intermediate values look random because XOR mixes bits unpredictably.

