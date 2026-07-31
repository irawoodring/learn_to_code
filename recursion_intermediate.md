# Intermediate Recursion — Memoization and Backtracking

By now you've written recursive functions to compute factorials, sum arrays, and maybe traverse a linked list or two. Those are examples of **direct recursion**, where a function solves a small piece of a problem and trusts a smaller call to itself to solve the rest.

This chapter goes a level deeper. We'll look at two ideas that show up constantly in technical interviews, competitive programming, and real software:

1. **Memoization** — caching recursive results so we never recompute the same subproblem twice.
2. **Backtracking** — a systematic way of exploring all possible solutions to a problem, abandoning ("backtracking out of") paths as soon as we know they can't work.

Both ideas depend on the same mental model: think of recursive calls as forming a **tree**. Memoization prunes *repeated* branches of that tree. Backtracking prunes branches that we determine can't lead to a solution. Once you can see the tree, both techniques become much more intuitive.

---

## The Call Tree

Consider the classic (and classically inefficient) recursive Fibonacci function:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

To compute `fib(5)`, the function calls `fib(4)` and `fib(3)`. But `fib(4)` *also* calls `fib(3)`. Draw it out and you get a tree like this:

```
                        fib(5)
                 /                \
            fib(4)                fib(3)
           /      \               /     \
       fib(3)     fib(2)      fib(2)    fib(1)
       /    \      /   \       /   \
   fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
   /   \
fib(1) fib(0)
```

Notice `fib(3)` appears **twice**, `fib(2)` appears **three times**, `fib(1)` appears **five times**. Each of those redundant calls re-does work that was already done somewhere else in the tree. As `n` grows, the number of redundant calls explodes.

Notice that every call to `fib(n)` (for `n > 1`) makes exactly two recursive calls, so the total number of calls roughly doubles the depth of the tree, which is `n`. That gives us:

$$T(n) = O(2^n)$$

This is **exponential time**. On most machines, `fib(30)` takes a noticeable fraction of a second, `fib(40)` takes several seconds, and `fib(50)` may not finish in your lifetime. The algorithm is *correct* — it's just wasteful, because it keeps solving the same subproblems from scratch.

This wastefulness is the signature of a problem that has **overlapping subproblems**: the same input to the function shows up over and over again in the recursion tree. Whenever you notice that pattern, memoization is likely to help.

## Memoization

**Memoization** (note: *memo*-ization, not "memorization" — it comes from "memo," as in a note you leave for yourself) is the technique of storing the result of a function call the first time you compute it, and looking it up instead of recomputing it every subsequent time.  We keep the natural recursive structure of the algorithm, but we wrap it in a cache.

### Memoized Fibonacci

Let's see how we can use memoization to speed up our recursive Fibonacci algorithm:

```python
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        return n

    result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    cache[n] = result
    return result
```

Let's walk through the logic.  First, we make sure the cache exists, and create one if it doesn't.  Then, we **check the cache for the values we need.** If we've already solved `fib(n)`, return the stored answer immediately — this is what eliminates the redundant work.  Otherwise, we check our base case as before. Then, call on the recursive case to calculate the values we don't have - but *before returning*, we store the result in the cache under key `n`.

With this change, the recursion tree effectively gets pruned: the first time we reach `fib(3)`, we solve it and store it. Every other branch that needs `fib(3)` gets an instant cache hit instead of re-expanding the whole subtree.

### Why This Is So Much Faster

Each distinct value of `n` from `0` to the original input is computed **exactly once**. Computing a new value takes constant time (one addition, one cache lookup, one cache write) once its two dependencies are known. This gives:

$$T(n) = O(n)$$

That's a drop from *exponential* to *linear* time — one of the most dramatic complexity improvements you'll see in this course. The tradeoff is space: we now use $O(n)$ extra memory for the cache, plus $O(n)$ stack space for the recursion depth. This is a classic **time-space tradeoff**, and in almost all practical situations, it's a fantastic trade.

| n  | Naive `fib(n)` calls (approx.) | Memoized `fib(n)` calls |
|----|-------------------------------|--------------------------|
| 10 | ~177                          | ~19                       |
| 20 | ~21,891                       | ~39                       |
| 30 | ~2,692,537                    | ~59                       |
| 40 | ~331,160,281                  | ~79                       |

The naive version's call count roughly doubles every time `n` increases by 1. The memoized version's call count grows by a small constant amount. This is the difference between a program that finishes instantly and one that never finishes.

### A Cleaner Pattern: Decorators

Python's standard library gives you memoization for free with a decorator, which is worth knowing about:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

`lru_cache` wraps the function so that every call with a given set of arguments is cached automatically. Behind the scenes, it's doing exactly what our hand-written `cache` dictionary did.  But now, we don't have to worry about it.  Our code stays nice and clean, and still looks almost identical to our mathematical definition of the Fibonacci function.

### Memoization vs. Tabulation

Memoization is *top-down*: you start from the original problem and recurse downward, caching as you go. There's a sibling technique called **tabulation**, which is *bottom-up*: you build a table starting from the base cases and iterate upward until you reach the answer, with no recursion at all.  Again, tabulation is not for recursion, but iteration (our "normal" way of looping).

```python
def fib_tabulation(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
```

Both approaches run in $O(n)$ time. Tabulation avoids recursion overhead and stack depth limits entirely, which can matter for very large inputs. Memoization is often more natural to *write*, since it mirrors the recursive definition of the problem directly. You'll see tabulation in more depth when you are in a course that covers dynamic programming formally — for now, just know the two names and how they relate.

### When Should You Use Memoization?

Ask yourself two questions about a recursive function:

1. **Does it call itself with the same arguments more than once** across different branches of the recursion tree? (Overlapping subproblems.)
2. **Does the function always return the same output for the same input** — i.e., no dependence on external mutable state? (This property is called being *pure* or *deterministic*.)

If the answer to both is "yes," memoization is a candidate. If a function is called with wildly different arguments every time (no repeats), memoization won't help — there's nothing to reuse.

---

## Backtracking

Memoization speeds up recursive algorithms that solve *one* well-defined value. Backtracking is different: it's a strategy for recursive algorithms that must **search through a space of possible solutions** — arrangements, combinations, placements — to find one (or all) that satisfy some constraint.

### The Basic Idea

Backtracking builds a solution incrementally, one choice at a time. At each step, it:

1. **Chooses** a candidate for the next piece of the solution.
2. **Checks** whether that choice is still valid given everything chosen so far.
3. **Recurses**, trying to extend the partial solution.
4. **Un-chooses** (backtracks) if the recursive call didn't lead to a solution, so it can try the next candidate instead.

The key insight that makes backtracking efficient is step 2: by checking validity *as early as possible*, we avoid wasting time exploring huge sections of the search tree that could never work anyway. This is called **pruning**.

A generic template looks like this:

```python
def backtrack(partial_solution):
    if is_complete(partial_solution):
        record_solution(partial_solution)
        return

    for choice in get_candidates(partial_solution):
        if is_valid(choice, partial_solution):
            make_choice(partial_solution, choice)      # choose
            backtrack(partial_solution)                 # recurse
            undo_choice(partial_solution, choice)        # un-choose
```

That "make choice → recurse → undo choice" part is the mainstay of every backtracking algorithm you'll write. If you can identify what a "choice" is, what makes a choice "valid," and what a "complete" solution looks like, you can turn almost any exhaustive search problem into a backtracking algorithm.

### First Example - Generating Permutations

Before tackling 8 queens (the classic backtracking problem), let's build intuition with something smaller: generating all permutations of a list.

```python
def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:	# Are there any numbers left?  If so, keep going (our base case)
            result.append(current[:])   # Copy all of the current numbers into result
            return
        for i in range(len(remaining)):		# For all remaining numbers
            current.append(remaining[i])	# Add the next one
            backtrack(current, remaining[:i] + remaining[i+1:])	# Recurse on the rest
            current.pop()               # undo the choice

    backtrack([], nums)
    return result
```

Trace `permutations([1, 2, 3])` on paper. Notice how `current.append` is the "choose" step and `current.pop()` is the "un-choose" step — we're literally reusing the same list object across branches, adding to it going down the tree and removing from it coming back up. This is more efficient than building a brand-new list at every level, and it's a pattern you'll see constantly in backtracking code.

Now that you have had a chance to trace it on paper (hopefully you stopped and did that!), here is a sample run:

```
Call: backtrack(current=[], remaining=[1,2,3])
- Branch i=0 → choose 1. current=[1], recurse with remaining=[2,3]
	- Branch i=0 → choose 2. current=[1,2], recurse with remaining=[3]
			- Branch i=0 → choose 3. current=[1,2,3], recurse with remaining=[]
				- remaining is empty → record [1,2,3]
			- undo: current.pop() → current=[1,2]
			- undo: current.pop() → current=[1]
	- Branch i=1 → choose 3. current=[1,3], recurse with remaining=[2]
		- Branch i=0 → choose 2. current=[1,3,2], recurse with remaining=[]
			- record [1,3,2]
		- undo: current.pop() → current=[1,3]
		- undo: current.pop() → current=[1]
	- undo: current.pop() → current=[]
	- Branch i=1 → choose 2. current=[2], recurse with remaining=[1,3]
		- choose 1 → current=[2,1], recurse with remaining=[3] → choose 3 → current=[2,1,3] → record [2,1,3] → pop, pop
		- choose 3 → current=[2,3], recurse with remaining=[1] → choose 1 → current=[2,3,1] → record [2,3,1] → pop, pop
		- undo → current=[]
	- Branch i=2 → choose 3. current=[3], recurse with remaining=[1,2]
		- choose 1 → current=[3,1], recurse with remaining=[2] → choose 2 → current=[3,1,2] → record [3,1,2] → pop, pop
		- choose 2 → current=[3,2], recurse with remaining=[1] → choose 1 → current=[3,2,1] → record [3,2,1] → pop, pop
		- undo → current=[]
Final result:

[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
```

All $3! = 6$ permutations, in the order the tree is explored left-to-right, depth-first. Notice the rhythm: append → recurse deeper → pop, exactly matching the choose/recurse/un-choose pattern from the backtracking template — the pop() after each recursive call is what lets current get reused cleanly across every branch instead of leaking state between them.

## The Eight Queens Problem

A classic recursive backtracking problem asks you to place 8 queens on a standard 8×8 chessboard so that **no two queens attack each other**. In chess, a queen attacks any square in the same row, same column, or same diagonal. Our job is to find an arrangement (or all arrangements) of 8 queens, one per row, so that none of these attack rules is violated.

This is a perfect backtracking problem because:
- A "choice" is naturally defined: *where do I place the queen in this row?*
- Validity is checkable incrementally: as soon as we place a queen, we can check it against every queen placed so far.
- We don't need to consider full boards that are already invalid — we can prune the moment a conflict appears.

### Key Simplification

Since no two queens can share a row, we know immediately that **each row gets exactly one queen**. That reduces our search from "choose 8 squares out of 64" down to "for each row, choose which column to place a queen in" — a much smaller space of $$8^8$$ possibilities before we even start pruning (and pruning will cut that down enormously).

We'll represent a board as a list `positions`, where `positions[row]` is the column of the queen in that row. For example, `positions = [0, 4, 7, 5, 2, 6, 1, 3]` means row 0 has a queen in column 0, row 1 has a queen in column 4, and so on.

### The Solution

```python
def solve_n_queens(n=8):
    """
    Returns a list of all valid board configurations.
    Each configuration is a list where index = row, value = column.
    """
    solutions = []
    positions = []  # positions[row] = column of the queen in that row

    def is_valid(row, col):
        for prev_row in range(row):
            prev_col = positions[prev_row]
            # same column?
            if prev_col == col:
                return False
            # same diagonal? (difference in rows == difference in columns)
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(positions[:])  # found a complete, valid board
            return

        for col in range(n):
            if is_valid(row, col):
                positions.append(col)     # choose
                backtrack(row + 1)         # recurse to the next row
                positions.pop()            # un-choose

    backtrack(0)
    return solutions


def print_board(positions):
    n = len(positions)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if positions[row] == col else ". "
        print(line)
    print()


if __name__ == "__main__":
    solutions = solve_n_queens(8)
    print(f"Total solutions found: {len(solutions)}")
    print("First solution:")
    print_board(solutions[0])
```

### Walking Through the Logic

**`is_valid(row, col)`** — Before placing a queen at `(row, col)`, we check it against every queen already placed in rows `0` through `row - 1`:
- **Same column check:** `prev_col == col`. We don't need to check rows, since we only ever have one queen per row.
- **Same diagonal check:** two squares are on the same diagonal exactly when the absolute difference in their row indices equals the absolute difference in their column indices. This one line handles *both* diagonal directions (`/` and `\`) at once. Take a moment and convince yourself of this with a small example: `(2, 3)` and `(4, 5)` — row difference is 2, column difference is 2, so they're on the same diagonal.

**`backtrack(row)`** — This is the main driver of the algorithm:
- **Base case:** if `row == n`, we've successfully placed a queen in every row without conflicts, meaning `positions` is a complete, valid solution. We save a *copy* of it (important — `positions[:]`, not `positions`, since `positions` keeps changing after this).
- **Recursive case:** for the current row, try every column `0` through `n - 1`. If placing a queen there is valid given everything above it, place it, recurse into the next row, and afterward remove it (`positions.pop()`) so the next candidate column can be tried cleanly.

**Why the `pop()` matters:** this is the "backtrack" step that gives the technique its name. If a recursive call into `backtrack(row + 1)` fails to find *any* valid completion, control returns here, we undo our choice, and we try the next column. Without popping, `positions` would still contain the failed choice, which would mean every future attempt is an invalid placement.  No need to continue adding queens to a board that is already invalid - prune the branch that led us down this path.

### Tracing a Small Example

It's easier to see the pruning in action on a 4×4 board (the "4 Queens" problem). Try placing a queen in row 0, column 0:

```
Row 0: Q . . .
```

For row 1, columns 0 and 1 are invalid (column 0 is taken; column 1 is diagonally adjacent). Column 2 works:

```
Row 0: Q . . .
Row 1: . . Q .
```

Now for row 2: column 0 is diagonal to row 1's queen, column 1 is diagonal to row 0's queen, column 2 is taken, and column 3 is diagonal to row 1's queen. **Every column fails.** This is a dead end — the algorithm backtracks out of row 2, back to row 1, and tries the next column there instead. This single backtrack step is exactly what saves us from exploring the (doomed) rest of that branch.

If you run this trace all the way through, 4 Queens has exactly **2 solutions**. The full 8×8 board has **92 solutions**, which `solve_n_queens(8)` will find in a fraction of a second, despite the search space technically containing $8^8$ (over 16 million) raw placements before pruning.

### Complexity

In the worst case, backtracking for N-Queens explores a search tree bounded by $O(N!)$ — at row 0 there are up to $N$ choices, row 1 has at most $N - 1$ remaining valid-ish choices, and so on. In practice, the diagonal and column checks prune the vast majority of branches long before they reach the bottom of the tree, which is why the algorithm is fast in practice even though its worst-case bound looks intimidating. This gap between "theoretical worst case" and "typical performance with good pruning" is a recurring theme in backtracking algorithms.

## Combining the Two Ideas

Memoization and backtracking solve different kinds of problems, but they can appear together. A common example is **backtracking with memoized validity checks** — for instance, in Sudoku solvers, you might cache which numbers are still legal for a given cell so you don't recompute that from scratch after every backtrack. More formally, some search-and-count problems (like counting the number of ways to place non-attacking pieces on constrained boards) combine backtracking's branching with a memo table keyed on some compressed representation of "state" (such as bitmasks representing occupied columns and diagonals) — that's a more advanced technique you'll encounter if you take a dedicated algorithms course, but it's good to know the two ideas aren't mutually exclusive.

A useful rule of thumb:

- If your recursion computes a **single value** and keeps recomputing the same subproblem → think **memoization**.
- If your recursion needs to **explore/construct many candidate solutions** under constraints → think **backtracking**.
- If both apply — you're solving a constrained counting problem — you may want both.

## Common Pitfalls

When solving these types of problems, it can be tricky to keep track of everything.  If you find that your algorithm isn't working, make sure you didn't make any of the following mistakes:

- **Forgetting to copy mutable state.** In both permutations and N-Queens, we appended `positions[:]` (a copy), not `positions` itself. If you store a *reference* to a mutable list that keeps changing, all your "saved" solutions will end up identical (and wrong) by the time the algorithm finishes.
- **Forgetting the "undo" step in backtracking.** If you don't pop/remove your choice after recursing, leftover state leaks into sibling branches, producing incorrect results that are maddening to debug.
- **Memoizing impure functions.** If a function's output depends on anything other than its arguments (global variables, mutable objects, I/O), caching its results can silently produce stale or wrong answers.  Memoization works when the same inputs produce the same outputs.
- **Mutable default arguments.** Notice `fib_memo(n, cache=None)` initializes `cache` inside the function body rather than writing `def fib_memo(n, cache={})`. Default mutable arguments in Python are created *once* (when the function is first parsed by Python) and shared across all calls that don't supply their own.  This is a classic bug that has nothing to do with recursion but loves to hide inside recursive helper functions.
