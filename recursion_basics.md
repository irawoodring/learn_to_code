# Recursion Basics

Recursion is often cited as one of the most "mind-bending" concepts for beginning programmers, yet it is one of the most elegant and powerful tools in a developer's arsenal. At its core, recursion is a programming (and math) technique where a function calls itself to solve a problem by breaking it down into smaller, simpler sub-problems.

In this chapter, we will deconstruct the mechanics of recursion, explore the mathematical foundations that make it possible, and learn how to think recursively to solve complex algorithmic challenges.

---

## The Conceptual Framework

An old programmer joke goes, "To understand recursion, you must first understand recursion".  Really though, to understand recursion, you must first shift your mental model of how code executes. Most programmers are taught **Iterative Thinking**: "How do I repeat this action until a condition is met?" - looping. To master recursion, you must adopt **Recursive Thinking**: "What is the simplest version of this problem, and how can I reduce the current version to that simpler one?"

We do this by identifying the following parts of the problem:

1.  **The Base Case:** The stopping condition. This is the smallest, simplest version of the problem that can be solved directly without any further recursion. Without a base case, a recursive function will call itself indefinitely, eventually crashing the program (resulting in a **stack overflow**).
2.  **The Recursive Step:** The part of the function where it calls itself. Crucially, this step must involve a smaller or simpler version of the original problem.
3.  **The Convergence:** The guarantee that every recursive step brings you closer to the base case.

We often illustrate this concept mathematically.  Consider the way you compute the Fibonacci sequence.  The first and second Fibonacci numbers are both 1.  Those are our base cases - they are defined and we don't need to compute them.  They are the simplest version of the problem.  From these, we calculate the rest by adding the previous 2 Fibonacci values together.  If we were keeping a table it would look like this:

|index|value|needed values |
|-----|-----|--------------|
| 0   |   1 | defined |
| 1   |   1 | defined |
| 2   |   2 | fib(1) + fib(0) |
| 3   |   3 | fib(2) + fib(1) |
| 4   |   5 | fib(3) + fib(2) |
| 5   |   8 | fib(5) + fib(4) |

and so on.  Notice that for the first two values we didn't perform any computation - the values were just defined.

When working from the **bottom-up**, i.e. starting at the base case and proceeding, students usually understand recursion pretty well.  Unfortunately, in computing we are often performing recursion from the **top-down**.  In our Fibonacci example, that simply means we are asked "What is the 5th Fibonacci number?" and we work backwards to our base case.  For some reason this switch in direction often throws students. But let's look at the table and see that it is really the same thing:

|index|value|needed values|
|-----|-----|-------------|
| 5   | 8   | fib(4) + fib(3) |
| 4   | 5   | fib(3) + fib(2) |
| 3   | 3   | fib(2) + fib(1) |
| 2   | 2   | fib(1) + fib(0) |
| 1   | 1   | defined |
| 0   | 1   | defined |

Nothing drastically different here, we just switched the order.  Instead of saying, "Hey computer start with the first two Fibonacci numbers, and follow the formula up to the 5th," we say "Hey computer, I need the 5th Fibonacci number. Compute all the ones before it going back to the defined values.  Then add the fourth and third together."  Mathematically, we could write this out as:

$$fib(0) = 1$$
$$fib(1) = 1$$
$$fib(n) = fib(n - 1) + fib(n - 2)$$

The first line is our recursive case - the function calling itself.  For instance, to calculate $fib(5)$ we need to add $fib(4)$ to $fib(3)$.  However, since we do't have those values yet, they must be caculated as well.  And so on, until we get to our base case(s).

What makes recursion so handy is that given the mathematical definition above, we can easily convert to code. In fact, the code is going to look almost exactly like our mathematical definition above:

```python
def fibbonacci(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)
```

See how closely the source code aligns?  It is virtually the same as our math definition, just written in Python!

*Warning:* This specific implementation is inefficient ($O(2^n)$ complexity) because it recalculates the same values multiple times. We will cover optimization later. We use it here only because it is an example students tend to be familiar with.

## Another classic - Factorials

Let's see another classic example - the factorial function.

The factorial of $n$ (written as $n!$) is the product of all positive integers less than or equal to $n$.

- **Mathematical Definition:** $n! = n \times (n-1) \times ... \times 1$
- **Recursive Definition:** $n! = n \times (n-1)!$ with base case $0! = 1$.

```python
def factorial(n):
    # Base Case: The simplest version of the problem
    if n <= 1:
        return 1
    
    # Recursive Step: Solve a smaller version (n-1)
    return n * factorial(n - 1)

print(factorial(5))  # Result: 120
```

*Trace:*
`factorial(3)` $\rightarrow$ `3 * factorial(2)` $\rightarrow$ `3 * (2 * factorial(1))` $\rightarrow$ `3 * (2 * 1)` $\rightarrow$ `6`.

## How the Computer Handles Recursion: The Call Stack

To understand why recursion works, we must understand what happens under the hood in memory. When a function is called, the computer allocates a "Stack Frame" in the **Call Stack**. This frame stores:

- Local variables.
- Parameters passed to the function.
- The return address (where to go back once the function finishes).

When a recursive function calls itself, a *new* stack frame is pushed onto the top of the stack. The current function's execution "pauses" while the new version waits for a result. 

**The Visualization:** Imagine a stack of plates. Every time you call the function again, you put a plate on top. Only when the base case returns a value does the top plate get removed, and the logic beneath it resume. If the stack grows too high (usually due to missing a base case), you hit a `RecursionError`.

Let's see how this might look for our `factorial()` function above.  Let's say the user asked for `factorial(5)` to be calculated.  Python will call the function, passing to it the parameter 5:

```
===============
| n=5         | factorial(5)
=====STACK=====
```

Since 5 is not less than or equal to 1, the base case does not run.  Python moves on to the recursive call, `n * factorial(n - 1)`, in this case `5 * factorial(4)`:

```
================
| n=4          | factorial(4)
===============
| 5 * ...      | factorial(5)
=====STACK======
```

The '...' above means that the `factorial(5)` stack frame is waiting for the call to `factorial(4)` to complete.  It will use whatever value the above function passes down to it to finish the calculation.  However, `factorial(4)` is going to call `factorial(3)`, and so on, resulting in a stack that looks like this:

```
================
| 1            | factorial(1)
================
| 2 * ...      | factorial(2)
================
| 3 * ...      | factorial(3)
================
| 4 * ...      | factorial(4)
================
| 5 * ...      | factorial(5)
=====STACK======
```

The top stack frame hits our base case - for $n=1$, the answer is just $1$.  No multiplication is needed.  Therefore, that function returns the 1, and the stack frame below it can finish its work:


```
================
| 2 * 1        | factorial(2)
================
| 3 * ...      | factorial(3)
================
| 4 * ...      | factorial(4)
================
| 5 * ...      | factorial(5)
=====STACK======
```

Then,


```
================
| 3 * 2        | factorial(3)
================
| 4 * ...      | factorial(4)
================
| 5 * ...      | factorial(5)
=====STACK======
```

```
================
| 4 * 6      | factorial(4)
================
| 5 * ...      | factorial(5)
=====STACK======
```

```
================
| 5 * 24       | factorial(5)
=====STACK======
```

And finally, `factorial(5)` returning $$5 * 24 = 120$$ - our final answer!

## Recursion in Data Structures

While loops are great for iterating over lists, **recursion** is the natural way to navigate non-linear data structures like Trees and Graphs.

### Tree Traversal
A Binary Tree is a structure where every node has at most two children. Because a tree is a recursive structure (each child of a node is itself the root of a smaller tree), recursion is the cleanest way to traverse it.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node):
    if node is None:
        return
    
    print(node.value)       # Process current node
    print_tree(node.left)    # Recurse left
    print_tree(node.right)   # Recurse right
```

This pattern (Process, then Recurse Left, then Recurse Right) is the backbone of **Depth-First Search (DFS)**.

## Performance, Memory, and Optimization

Recursion is beautiful, but it isn't always the fastest way to get a result.  Python has a default stack frame limit (usually 1000). If you try to calculate `factorial(2000)`, Python will raise a `RecursionError`. This is a safety feature to prevent your program from crashing the entire OS by consuming all available memory in the stack.

One of the biggest pitfalls in recursion (like the Fibonacci example) is **redundant work**. If you call `fib(5)`, it calls `fib(4)` and `fib(3)`. But `fib(4)` *also* calls `fib(3)`. You are calculating the same thing twice.  We can fix this issue with **memoization**.  Memoizationi is storing the results of function calls so they can be used later.

```python
# Using Python's built-in decorator for memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n <= 1:
        return n
    return fibonacci_fast(n - 1) + fibonacci_fast(n - 2)
```
This turns an exponential-time algorithm ($O(2^n)$) into a linear-time algorithm ($O(n)$).

## When to use Recursion vs. Iteration

The "Recursion vs. Loops" debate is common. Here is the rule of thumb:

**Use Recursion when:**
1.  **The problem has a recursive structure:** If you are working with Trees, Graphs, or File Systems (folders inside folders), recursion is almost always cleaner.
2.  **Divide and Conquer:** If the logic involves splitting a list into halves recursively (like Merge Sort).
3.  **Code Clarity:** When the recursive solution is significantly more readable and easier to maintain than a complex loop with multiple state variables.

**Use Iteration when:**
1.  **Performance is critical:** Loops generally have less overhead than function calls.
2.  **Deep Depth requirements:** If you need to process 10,000 items in a linear sequence, recursion will hit the limit; a loop won't.
3.  **State-heavy processing:** If you are maintaining multiple pointers/indices that move independently (like a sliding window).

---

## Real World Applications: The File System

One of the best ways to see recursion in action is by traversing a computer's hard drive. Every folder can contain files and more folders, which can contain more files... this is an infinite recursive structure.

```python
import os

def list_files_recursive(path):
    print(f"Scanning: {path}")
    for entry in os.scandir(path):
        if entry.is_dir():
            # The directory is found! Now, recursively call this function on the subdirectory.
            list_files_recursive(entry.path)
        else:
            print(f" - File: {entry.name}")

# Usage: list_files_recursive('/Users/woodriir/Documents')
```
This is exactly how your operating system's "search" functionality works. It doesn't care how deep the folders go; it just keeps asking, "Are there more folders here? If so, do the same thing on those."

