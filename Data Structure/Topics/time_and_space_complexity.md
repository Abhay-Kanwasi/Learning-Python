# Time Complexity
Time complexity is a way to measure how much time an algorithm takes to run as the input size grows.

In simple terms:
> It tells you how the running time of your code increases when the input gets bigger.

### Rules
1. Always calculate time complexity of worst case. 

    We consider worst case because it gives a guarantee that the algorithm will never perform slower than this, no matter the input. This makes it reliable for real-world systems where slow performance can cause failures.

    We have multiple cases of time complexity:

    - <b>Best Case</b>
        
        The minimum time an algorithm takes, when the input is in the most favorable state. It's denoted by `Omega (Ω)`

        It's also called upper bound.

        <b>Example</b>: Linear search for a value in a list
        If the target is the first element, you find it in 1 step.

       >  Best case: O(1)

    - <b>Average Case</b>

        The expected time when the input is randomly distributed (neither best nor worst). It's denoted by `Theta (θ)`

        <b>Example</b>: Linear search

        On average, you find the element somewhere in the middle.

        > Average case: O(n)

    - <b>Worst Case</b>
        The maximum time an algorithm takes, when the input is in the least favorable state. It's denoted by `Big Oh (O)` 

        It's also called lower bound.
        
        <b>Example</b>: Linear search

        If the target is the last element (or not present at all), you check every element.

        > Worst case: O(n)

2. Avoid the constant values.

    We avoid constant values because Big-O measures how time grows with input size, not exact time — constants don't affect the growth rate. For large inputs, the growth pattern (n, n², log n) matters far more than small constant factors like 2 or 100.

3. Avoid lower bounds

    We avoid lower-order terms because for large inputs, the highest-order term dominates the growth — smaller terms become negligible. For example, in n² + n + 5, when n = 1000, the n² part (1,000,000) makes n (1000) and 5 insignificant.



# Space Complexity
Total memory an algorithm needs to run, as a function of input size n.

```text
Space Complexity = Auxiliary Space + Input Space
```

- Input Space

    Memory used to store the input itself.

    Example:

    ```python
        arr = [1, 2, 3, ..., n]   # takes O(n) space
    ```
    This is the space for the data you're given.

- Auxiliary Space

    Extra/temporary memory used by the algorithm besides the input.

    Example:
    ```python
    def sum(arr):
        total = 0          # 1 variable → O(1) auxiliary
        for x in arr:
            total += x
        return total
    ```
    Here, total is auxiliary space = O(1).


### Putting It Together

| Component | Meaning | Example |
|-----------|---------|---------|
| **Input Space** | Space for input data | Array of size n → O(n) |
| **Auxiliary Space** | Extra temp space | Variables, new arrays, recursion stack |
| **Total Space** | Input + Auxiliary | O(n) + O(1) = O(n) |