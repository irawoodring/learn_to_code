# The Language of Complexity - Big-O Notation and Algorithmic Analysis

In the realm of software engineering, writing code that *works* is the baseline requirement. Writing code that *scales* is the hallmark of a professional. As datasets grow from dozens to billions of records, the difference between an algorithm that finishes in milliseconds and one that takes centuries can be the difference between a successful product and a failed project.

This chapter introduces **Big-O notation**, the language we use to describe how an algorithm's resource requirements (usually time and memory, but can be any resources) grow as the input size increases.

## The Core Intuition: Growth Rates

Before we dive into formal mathematics, let's establish a mental model. When we analyze an algorithm, we aren't interested in exact numbers of operations—like "How many CPU cycles did this loop take?" Because computer processors work differently depending on the brand and architecture, this wouldn't make sense for us to measure.  Instead, we care about **Growth Rate**.

Imagine you are tasked with finding a specific name in a phone book of $n$ people.
- If the book is sorted alphabetically, you can start at the beginning and flip pages until you find it. If there are 100 names, it might take 50 flips. If there are 1,000,000 names, it might take 500,000 flips. The time grows linearly with the size of the book ($n$).
- If you can jump to the middle of the book, see if the name comes before or after that point, and discard half the remaining pages each time, you'll find the name much faster. For 1,000,000 names, this method (called "binary search") takes only about 20 flips.

Big-O notation allows us to describe these behaviors: **Linear**, **Logarithmic**, **Quadratic**, etc.  You should remember these terms from an Algebra or Pre-Calculus class.  They are the words we use to describe functions.

## Formal Definition of Big-O

**Big-O Notation** represents the **upper bound** of an algorithm's complexity. It describes the "worst-case scenario" for how the execution time (or space, or whatever resource) grows as the input size $n$ approaches infinity.

Mathematically, we say $f(n)$ is $O(g(n))$ if there exist positive constants $c$ and $n_0$ such that:
$$0 \le f(n) \le c \cdot g(n) \text{ for all } n \ge n_0$$

In plain English: "For sufficiently large inputs, the actual running time of our algorithm is **never more than** some constant multiple of $g(n)$."  What this statement implies is that if we have a function that describes our algorithm's growth, such as $2n^2 + 3n + 5$, that all we really care about is our highest order term.  We can drop anything below that, and we can drop constant multipliers.  Here we would say, $2n^2 + 3n + 5$ is $O(n^2)$.

### Why ignore constants?

When $n$ is 1,000,000, the difference between an algorithm that takes $2n$ operations and one that takes $100n$ operations is negligible compared to the difference between a linear algorithm ($n$) and a quadratic algorithm ($n^2$). As $n \to \infty$, the highest-order term dominates everything else.  And since Big-O is concerned with the worst case scenario, we always think about what happens as our input size grows to infinity.

Now, some of you are probably thinking, "Well yeah, but what about the best case or average case?"  We measure those as well, though we won't go into it in this course.  Often a worst case measurement is enough for us when choosing between multiple algorithms.  In the situation in which two algorithms have the same worst case performance, we might then want to examine best or average case.  But let's master calculating the worst case first!

## Calculating Complexity

Ok, so you've written a great new function and you want to compute its runtime Big-O.  Where do we start?  Well, we need to figure out a number of operations that each line requires.  Now again, under the hood, processors are going to do things differently.  But that's ok; we simply need to be consistent in how we measure. First, we need to define a few **Atomic Operations**.  These are operations that we can reasonably assume take constant - O(1) time.  We are going to use these operations:

| Atomic Operation | Example | Count |
|------------------|---------|------:|
| Assignment | `x = 5` | 1 |
| Variable read | `y = x` (read `x`) | 1 |
| Variable write | `x = y` (write `x`) | 1 |
| Arithmetic | `x + y`, `a * b`, `n - 1` | 1 |
| Comparison | `x < y`, `a == b`, `i <= n` | 1 |
| Boolean operation | `&&`, `||`, `!` | 1 |
| Array indexing | `arr[i]` | 1 |
| Function return | `return x` | 1 |
| Constant access | `5`, `'a'`, `true` | 1 |

You'll find subtle variations between how people compute Big-O.  That can be confusing; the truth is though, that it doesn't matter that much.  As long as we are consistent in our measurements, we can then compare two algorithms and make the informed choice.  Think of it like this - suppose there are two classrooms and we want to know which one has the most people inside.  It doesn't matter if we count the number in room one by ones and room two by ones and compare, or we count the number in room one by fives and room two by fives and compare.  As long as we used the same value (both counted by ones or both counted by fives), we can still tell which room had more people in it.

Ok, so now we have a list of atomic operations.  Let's apply it!  Given the algorithm:

```python
def my_cool_function(numbers: list[int], size: int):
  total = 0
  total = total + numbers[0]
  total = total + numbers[size - 1]
  print(total)
  return
```

This function isn't particularly useful, but we can still calculate its Big-O.  The first line we could say takes 1 operation.  We are simply assigning a value to a variable.  The next line has a lot more going on though!  We see an array indexing operation (`numbers[0]`).  Then, an addition operation.  Finally, an assignment.  Together, that makes 3 atomic operations for the line.

The next line is even more complex; we have a subtraction (`size - 1`), then an array indexing, an addition, then an assignment.  So this line gets 4 operations.  The next line is simply a print statement, so just 1 op.  Same thing with the `return`.  If we listed the number of operations per line to the left of the code, we would have:

```python
  def my_cool_function(numbers: list[int], size: int):
1   total = 0
3   total = total + numbers[0]
4   total = total + numbers[size - 1]
1   print(total)
1   return
``` 

The total would be 10 operations.  That means our function would be $f(x) = 10$.  There are no variables in that function - only a constant, which means that the runtime doesn't increase as x (the size of our input data) gets larger.  Therefore, this function is $O(1)$ or constant time.

Let's change it around a bit though.  Imagine that we instead had this function:

```python
def my_cool_function(numbers: list[int], size: int):
  total = 0
  for number in numbers:
    total = total + number
  return total
```

This function is a bit more complex; it has a loop.  So how do we handle loops?  We simply need to determine how many times it runs.

Now, this Python-style for-loop is a bit more complex than loops in other languages.  This loop is really a for-each loop - it runs once for each of the values in the numbers list.  If this were C, we would see that this requires creating a temporary variable, indexing into the array, etc.  The "correct" way to compute the Big-O here would be to convert this loop to a more C-style loop.  However, we really don't need to be that exact for Big-O (we would be more concerned with getting this right if we were computing the average or best case scenarios).  For our purposes, we are going to say this loop runs $n$ times - once for each of the $n$ numbers in the list.  Again, purists might not like it, but it gives us a close-enough estimate to be able to compare the Big-O of this algorithm to another.

Ok, so what about the line inside the loop?  Well, since the loop is running $n$ times, this line will run $n$ times also.  However, this line isn't just 1 atomic operation - it is an addition and an assignment, so it is 2 operations.  Since those 2 operations are running $n$ times, we must multiply to see how many times this line runs.  Therefore, we can say this line runs $2n$ times.  Let's see what we've got now:

```python
  def my_cool_function(numbers: list[int], size: int):
1   total = 0
n   for number in numbers:
2n    total = total + number
1   return total
```

Adding it up gives us $3n + 2$ operations.  Since we can drop the constants and lower-order terms, we are left with $O(n)$ operations in the worst case.  So this function's growth rate is linear.  As the size of our list passed in gets bigger, the number of operations we must perform grows linearly.

## A Note on Loops

When students first start calculating Big-O they tend to think - oh a loop.  It must run $n$ times.  However, that is not always the case!

Consider this case:

```python
def my_other_cool_function(numbers: list[int], size: int):
  total = 0
  i = 1
  while i < len(numbers):
    total = total + numbers[i]
    i = i * 2
  return total
```

This code also has a loop.  If you don't look carefully, you might think, "Oh, it starts at 1 and goes up to the length of the list."  And that is true!  However, it doesn't get from 1 to the length of the list by adding 1 each time  Instead, it multiplies by 2.  If we start a 1 and continuously multiply by 2 until we get to some value n, we are skipping a lot of numbers.  The sequence of `i` would be 1, 2, 4, 8, 16, 32, 64, 128, 256, on and on until we got to $n$.  So how many times does that loop run?  We know that repeated multiplication can be expressed through exponentiation.  So $2^y$ would be multiplying by 2 $y$ times.  Here we are asking, "to get to some number $n$, what is the value of $y$ when multiplying by 2 each time?"  Mathematically, we are solving $y = log_2 n$.  Therefore, this loop runs $O(log_2 n)$ times.

I teach students to always make a table when they encounter a loop.  The table should have three rows - the value we start at, the value we end at, and how we got from the start to the end.  Once we know all three of those pieces of the puzzle, we can compute how many times the loop ran.

## Common Complexity Classes (The Hierarchy)

We call a function's growth rate its **Complexity Class**.  Here are some of the most common complexities you will encounter, ranked from fastest to slowest:

### O(1) - Constant Time
The execution time does not depend on the input size. It is the "Holy Grail" of efficiency.
*   **Example:** Accessing an element in an array by index, or pushing/popping from a stack.
*   **Code Example:**
    ```python
    def get_first_element(items):
        return items[0] # Always takes 1 step regardless of list size
    ```

### O(log n) - Logarithmic Time
The execution time grows proportionally to the number of times you can divide $n$ by 2. This is typical of "divide and conquer" algorithms where you discard half of the search space at each step.
*   **Example:** Binary Search.
*   **Code Example:**
    ```python
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target: return mid
            elif arr[mid] < target: low = mid + 1
            else: high = mid - 1
        return -1
    ```

### O(n) - Linear Time
The execution time grows in direct proportion to the input size. If you double the data, it takes twice as long.
*   **Example:** Searching for a value in an unsorted list (Linear Search).
*   **Code Example:**
    ```python
    def find_item(items, target):
        for item in items:
            if item == target:
                return True
        return False
    ```

### O(n²) - Quadratic Time
The execution time grows proportionally to the square of the input size. If you double the data, it takes four times as long. This is common in algorithms with nested loops over the same collection.
*   **Example:** Bubble Sort, Selection Sort.
*   **Code Example:**
    ```python
    def print_pairs(items):
        for i in items:
            for j in items:
                print(f"Pair: {i}, {j}")
    ```

### O(2ⁿ) - Exponential Time
The execution time doubles with every single addition to the input. These algorithms quickly become unusable for anything but tiny inputs.
*   **Example:** Solving the Towers of Hanoi, or recursive Fibonacci without memoization.

Now, this certainly isn't all of them.  Any function growth rate is possible.  These are just some common examples.

## Practice: Analyzing Code Complexity

Let's analyze a few more complex scenarios.

### Example A: The "Hidden" Linearities
```python
def process_data(items):
    # O(n) - Iterating once
    for item in items:
        print(item)
        
    # O(n) - Another iteration
    for item in items:
        process_logic(item)

# Total Complexity: O(n + n) = O(n)
```
*Rule:* We drop the coefficients. $O(2n)$ simplifies to $O(n)$.

### Example B: Nested Loops with Different Inputs
What is the complexity if we have a list of `users` and a list of `permissions`?
```python
def check_all_permissions(users, permissions):
    for user in users:           # Runs U times
        for perm in permissions: # Runs P times
            if user.has_access(perm):
                print("Access Granted")

# Total Complexity: O(U * P)
```
In Big-O, we represent this as $O(n \cdot m)$ where $n$ is the size of `users` and $m$ is the size of `permissions`. If both lists are the same size ($n$), it becomes $O(n^2)$.

---

## Space Complexity: The Memory Footprint

Big-O applies to memory just as much as time. **Space Complexity** measures the extra memory an algorithm allocates relative to the input size.

*   **O(1) Space:** You only use a few variables regardless of how big the input is.
    ```python
    def find_max(numbers):
        max_val = numbers[0] # O(1) space
        for n in numbers:
            if n > max_val:
                max_val = n
        return max_val
    ```
*   **O(n) Space:** You create a new list/dictionary that scales with the input.
    ```python
    def count_frequencies(items):
        freq_map = {} # O(n) space potentially
        for item in items:
            freq_map[item] = freq_map.get(item, 0) + 1
        return freq_map
    ```

---

## Summary Table of Common Growth Rates

| Notation | Name | Growth Rate (Small $n$) | Growth Rate (Large $n$) | Example |
| :--- | :--- | :--- | :--- | :--- |
| **O(1)** | Constant | Very Fast | Extremely Fast | Array Access |
| **O(log n)** | Logarithmic | Fast | Fast | Binary Search |
| **O(n)** | Linear | Moderate | Moderate | Linear Scan |
| **O(n log n)** | Linearithmic | Slow | Slow | Merge Sort |
| **O(n²)** | Quadratic | Very Slow | Extremely Slow | Nested Loops |
| **O(2ⁿ)** | Exponential | Terrible | Impossible | Recursive Fibonacci |

So, when you write a function, your first thought should be: *"What happens if I give this a million items?"* 

If your solution is $O(n^2)$, it might work fine for a school project with 100 inputs, but it will crash or hang in production when the user base grows. By mastering Big-O, you gain the ability to predict performance before a single line of code ever runs. You stop guessing and start engineering.
