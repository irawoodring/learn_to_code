---
author: ""
---

# Glossary

**2D Array/2D List**

An list of lists, representing a grid or table. Accessed with two indices: `matrix[row][col]`.

**Abstract Class**

A class that cannot be instantiated. May contain abstract methods (no body) that subclasses must implement.

**Abstract Method**

A method with no body, declared in an abstract class or interface. Forces subclasses to provide an implementation.

**Algorithm**

A finite, ordered set of well-defined steps for solving a problem or accomplishing a task. Algorithms must terminate, be unambiguous, and produce a result.

**Argument**

The actual value passed to a method when it is called: greet("Alice").

**Arithmetic Operators**

```python
+ (add)
 - (subtract)
 * (multiply)
 / (divide)
 % (modulus — remainder of division).
 ```

**Array Declaration & Initialization**

scores = []          // declares an empty array
grades = [90, 85, 92, 78, 88] // declares and initializes an array

**Array Traversal**

Visiting every element, usually with a loop.

**Array/List**

A fixed-size, ordered collection of elements of the same data type. Elements are accessed by zero-based integer index.

**Assignment**

Storing a value into a variable using `=`. The right side is evaluated first, then stored in the left side.  Note that `=` is different from `==` which is the comparison operator.

**Backtracking**

Explores all possibilities by building a solution incrementally and abandoning a path ("backtracking") as soon as it's determined to be invalid. Used for puzzles, constraint satisfaction (e.g. N-Queens, Sudoku).

**Base Case**

The condition under which a recursive method returns without making another recursive call. Every recursive method must have at least one base case.

**Best / Average / Worst Case**

An algorithm's performance can differ depending on the input. Big-O usually describes the worst case; Θ (Theta) describes the average; Ω (Omega) describes the best.
Core Data Structures

**Big-O Notation**

Describes the worst-case upper bound of an algorithm's growth rate. Ignores constants and lower-order terms.

 | Big-O         | Name              | Typical Meaning                         | Example                             |
| ------------- | ----------------- | --------------------------------------- | ----------------------------------- |
| {math}`O(1)`        | Constant Time     | Runtime does not grow with input size   | Array index lookup                  |
| {math}`O(\log n)`  | Logarithmic Time  | Grows slowly as input increases         | Binary search                       |
| {math}`O(\sqrt{n}` | Square Root Time  | Common in factorization algorithms      | Trial division prime checking       |
| {math}`O(n)`       | Linear Time       | Runtime grows directly with input size  | Single loop through a list          |
| {math}`O(n \log n)` | Linearithmic Time | Efficient divide-and-conquer scaling    | Merge sort, heap sort               |
| {math}`O(n^2)`    | Quadratic Time    | Nested iteration over data              | Bubble sort                         |
| {math}`O(n^3)`     | Cubic Time        | Triple nested loops                     | Naive matrix multiplication         |
| {math}`O(n^k)`      | Polynomial Time   | General polynomial growth               | Many dynamic programming algorithms |
| {math}`O(2^n)`   | Exponential Time  | Doubles with each added input element   | Recursive subset generation         |
| {math}`O(n!)`       | Factorial Time    | Extremely fast growth from permutations | Traveling salesman brute force      |


**Binary Search**

Repeatedly halves the search range by comparing the target to the midpoint. O(log n). Requires sorted data.

**Binary Search Tree (BST)**

A binary tree where every node's left subtree contains only values less than the node, and the right subtree contains only values greater. Enables {math}`O(log n)` search, insert, and delete on a balanced tree.

**Binary Tree**

A tree where each node has at most two children: left and right.

**`break`**

Python loop control statement that immediately exits the nearest enclosing loop or switch.

**Bubble Sort**

Repeatedly swaps adjacent elements that are out of order. Simple but slow.

**Call Stack**

The stack of active method calls. Each recursive call adds a frame; each return removes one. Too many recursive calls cause a stack overflow.

**Casting (Type Conversion)**

Converting a value from one data type to another. Implicit casting happens automatically (e.g. int → double). Explicit casting requires the programmer to specify it: int(3.9) → 3.

**Class**

A blueprint or template for creating objects. Defines the structure and behavior shared by all instances.

**Compilation**

The process of translating source code into machine code (binary) that a computer can execute directly. Performed by a compiler.

**Compound Assignment**

Shorthand that combines an operation with assignment: `x += 5` is equivalent to `x = x + 5`.

**Concrete Class**

A class that provides implementations for all methods (not abstract). Can be instantiated.

**Conditional Statement**

(`if` / `elif` / `else`) Executes a block of code only if a condition is true.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```


**Constant**

A variable whose value cannot change after it is assigned. Declared with final (Java), const (JavaScript), or by convention in ALL_CAPS.


**Constructor**

A special method called when an object is created (new). Initializes the object's fields. Has the same name as the class and no return type.  In Python is always named `__init__` (notice there are two underscores both before and after the word 'init').


**`continue`**

Python loop control statement that skips the rest of the current loop iteration and moves to the next one.

**Data Type**

Specifies the kind of value a variable can hold and the operations that can be performed on it.  In Python, the built-in types are:

```{table} Python Built-in Types
:name: python-builtin-types

| Category | Type | Description | Example |
|:---------|:-----|:------------|:--------|
| **Numeric** | `int` | Integer of unlimited precision | `42`, `-7`, `0` |
| **Numeric** | `float` | IEEE 754 double-precision float | `3.14`, `-0.5` |
| **Numeric** | `complex` | Complex number with real and imaginary parts | `3+4j` |
| **Numeric** | `bool` | Boolean subclass of `int` | `True`, `False` |
| **Sequence** | `str` | Immutable sequence of Unicode characters | `"hello"` |
| **Sequence** | `bytes` | Immutable sequence of bytes | `b"hello"` |
| **Sequence** | `bytearray` | Mutable sequence of bytes | `bytearray(b"hi")` |
| **Sequence** | `list` | Mutable ordered sequence | `[1, 2, 3]` |
| **Sequence** | `tuple` | Immutable ordered sequence | `(1, 2, 3)` |
| **Sequence** | `range` | Immutable sequence of integers | `range(0, 10)` |
| **Mapping** | `dict` | Mutable key-value pairs | `{"a": 1}` |
| **Set** | `set` | Mutable unordered collection of unique items | `{1, 2, 3}` |
| **Set** | `frozenset` | Immutable unordered collection of unique items | `frozenset({1, 2})` |
| **Binary** | `memoryview` | Memory buffer interface to binary data | `memoryview(b"hi")` |
| **Null** | `NoneType` | Represents the absence of a value | `None` |
```

**Debugging**

The process of finding, analyzing, and fixing errors in a program.

**Declaration**

Introducing a variable to the program by stating its name and (in some languages) its type.  For instance in Java we might create an integer with:

```Java
int x;
```

In Python we aren't required to provide the type, as Python determines it automatically.  However, we can provide type hints to provide context for other programmers:

```Python
x = 42
```

or

```python
x: int = 42
```

**Depth of a Node**

The number of edges from the root to that node.

**Dictionary (HashMap)**

Stores key-value pairs. Uses a hash function to compute an index into an array. {math}`O(1)` average for insert, delete, and lookup.

**Divide and Conquer**

A problem-solving strategy: split the problem into smaller subproblems, solve each recursively, combine the results. Used by merge sort, quicksort, and binary search.

**Dot Notation**

Accessing a field or calling a method on an object: myDog.bark(), circle.radius.

**Doubly Linked List**

Each node has two pointers: to the next and previous nodes. Allows traversal in both directions; {math}`O(1)` delete given a node reference.

**Encapsulation**

Bundling data and methods together and restricting direct access to internal state. Achieved via access modifiers and getter/setter methods.

**Exception**

Handling Responding to runtime errors gracefully using try, catch, finally, and throw rather than crashing.

**Field (Instance Variable)**

A variable defined inside a class that holds state for each object. Each instance has its own copy.

**`for`**

A loop that loops over all items in a collection.  For instance:

```python
for item in my_list:
  ... do something ...
```

Or,

```python
for index in range(0, len(my_list)):
  ... do something ...
```



**Formatted Output**

Controlling how values are displayed: print(f'The value is {number:.2f}.") prints to two decimal places.

**Getter / Setter**

Public methods used to read (`get_x()`) or write (`set_x(val)`) a private field, allowing controlled access.


**Greedy Algorithm**

Makes the locally optimal choice at each step, hoping to reach the global optimum. Works for some problems (e.g. Dijkstra's, Huffman coding) but not all.

**Head / Tail**

The first (head) and last (tail) nodes of a linked list.

**Heap Sort**

Builds a max-heap, then repeatedly extracts the maximum to sort in place. Guaranteed {math}`O(n log n)`.

**Height of a Tree**

The number of edges on the longest path from the root to a leaf.

**In-Place Sort**

Sorts using {math}`O(1)` extra memory (beyond the input array). Quicksort and heap sort are in-place; merge sort is not.

**Index**

The position of an element in an array, starting at 0. The last element is at index length - 1.

**Infinite Loop**

A loop whose condition never becomes false. Usually a bug, but sometimes intentional (e.g. a server listening for requests).

**Inheritance**

A class (subclass) extends another class (superclass), inheriting its fields and methods. Promotes code reuse.

**Initialization**

Assigning a value to a variable for the first time: `count = 0`.

**Insertion Sort**

Builds a sorted portion one element at a time. Efficient for nearly-sorted data.


**Instance**

A specific object created from a class: 

```python
myDog = Dog("Rilla", "Golden Retriever")
```

**Integer Division**

Division that truncates the decimal.  In Python used via the `//` operator: `7 // 2 = 3`.

**Interface**

A contract specifying what methods a class must implement, without providing an implementation.

**Interpretation**

Executing source code line-by-line at runtime, without a separate compilation step. Performed by an interpreter (e.g. Python, JavaScript).

**`isinstance`**

Checks whether an object is an instance of a particular class or interface before using: 

```python
if isinstance(my_dog, Dog):
  ... do something ...
```

**Iterator**

An object that traverses a collection one element at a time. Decouples traversal logic from the collection.

**Leaf**

A node with no children.

**Linear Search**

Checks every element in order until the target is found. {math}`O(n)`. Works on unsorted data.


**Linked List**

A sequence of nodes, each storing a value and a pointer to the next node. {math}`O(1)` insert/delete at head; {math}`O(n)` access by index.

**Literal**

A fixed value written directly in code (e.g. `42`, `3.14`, `"hello"`, `True`).


**Logic Error**

A bug where the program runs without crashing but produces incorrect results due to flawed reasoning in the code.

**Logical Operators**

Operators that combine boolean expressions: `and`, `or`, `not`.

**`match`**

Statement that selects one of many branches based on the value of an expression. Cleaner than a long `if` / `elif` / `else` chain when testing a single variable against multiple constant values.  Example:

```python
def get_day_name(day_number):

    match day_number:
        case 1:
            return "Monday"

        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"

        case 4:
            return "Thursday"

        case 5:
            return "Friday"

        case 6:
            return "Saturday"

        case 7:
            return "Sunday"

        case _:
            return "Invalid day"


print(get_day_name(3)) → Wednesday
print(get_day_name(7)) → Sunday
print(get_day_name(99)) → Invalid day
```

**Memoization**

Caching the results of expensive recursive calls so they aren't recomputed. A key technique in dynamic programming.


**Merge Sort**

Divides array in half recursively, sorts each half, then merges. Guaranteed {math}`O(n log n)`. Divide-and-conquer.

**Method (Function)**

A named, reusable block of code that performs a specific task. Reduces repetition and improves readability.  Technically a method belongs to an object or class, and a function does not.  However, the terms have become mostly interchangeable.


**Method Overloading**

Defining multiple methods with the same name but different parameter lists. The compiler picks the right one based on the arguments.  Python doesn't allow this; instead it provides default parameters.

**Method Overriding**

A subclass provides its own implementation of a method defined in the superclass. The method signature must match exactly.

**Method Signature**

The combination of a method's name and its parameter list.

**Modulo (%)**

Returns the remainder after integer division. `10 % 3 = 1`. Useful for checking even/odd, cycling through indices, etc.

**Node**

The basic building block of linked lists, trees, and graphs. Contains data and one or more pointers (references) to other nodes.

**`None`**

A special value indicating that a reference variable does not point to any object.


**None Method**

A method that performs an action but returns no value.


**Object**

An instance of a class. Combines data (fields) and behavior (methods) into a single unit.


**Operator Precedence**

The order in which operators are applied. Follows PEMDAS-like rules: `*`, `/`, `%` before `+`, `-`; use parentheses to override.  Official documentation can be found [here](https://docs.python.org/3/reference/expressions.html).

**Parameter**

A variable listed in a method's definition that receives a value when the method is called: void greet(String name).


**Parent / Child**

A node with connections below it has children; the node above is its parent.

**Polymorphism**

The ability of a variable to refer to objects of different types. A superclass reference can point to a subclass object, and the correct method is called at runtime.

**Program**

A sequence of instructions written in a programming language that a computer can execute.

**Prompt**

A message displayed to the user asking for input: 

```python
input("Enter your name: ");
```

**Queue**

A FIFO (First-In, First-Out) collection. Operations: enqueue (add to back), dequeue (remove from front). Used for BFS, task scheduling, buffers.

**Quicksort**

Picks a pivot, partitions the array into elements less than and greater than the pivot, recurses on each partition. O(n²) worst case with bad pivot choice; {math}`O(n log n)` on average.

**Recursion**

A method that calls itself to solve a smaller version of the same problem.

**Recursive Case**

The part of the method that reduces the problem and makes a recursive call.

**Relational Operators**

Operators used for comparisons:

```{table} Python Relational Operators
:name: python-relational-operators

| Operator | Name | Example | Result |
|:--------:|:-----|:--------|:-------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `3 >= 5` | `False` |
| `is` | Identity | `x is None` | `True` if same object |
| `is not` | Negated identity | `x is not None` | `True` if different objects |
```

**Return Value**

The value a method sends back to its caller. In Python, a function without a return automatically returns `None`.

**Root**

The topmost node of a tree; has no parent.

**Runtime Error**

An error that occurs while the program is running (e.g. dividing by zero, accessing a null reference). Also called an exception.

**Scope**

The region of code where a variable is accessible. In Python scope is created by indenting code after a colon ':'.

**Selection Sort**

Finds the minimum element and places it at the front. Always {math}`O(n²)` comparisons.

**`self`**

Keyword Refers to the current object inside a method or constructor. Used to distinguish instance fields from local variables with the same name.

**Semantics**

The meaning of syntactically valid statements — what a program actually does when it runs.

**Set**

A collection of unique elements with no defined order.

**Short-Circuit Evaluation**

In `A and B`, if `A` is `False`, `B` is never evaluated. In `A or B`, if `A` is `True`, `B` is never evaluated.

**Singly Linked List**

Each node has one pointer: to the next node. Traversal is one-directional.

**Source Code**

Human-readable instructions written by a programmer in a programming language (e.g. Python, Java, C++).


**Space Complexity**

A measure of how much memory an algorithm uses relative to input size.

**Stable Sort**

Preserves the relative order of equal elements. Merge sort is stable; quicksort and heap sort typically are not.

**Stack**

A LIFO (Last-In, First-Out) collection. Imagine a stack of dinner plates; you wouldn't want to pull one from the bottom of the stack.  Instead, we always take from the top (the last one placed down).

**Stack Frame**

The block of memory allocated on the call stack when a method is invoked. Stores local variables and parameters. Freed when the method returns.

**Stack Overflow**

A runtime error caused by infinite or extremely deep recursion, exhausting the call stack.

**Standard Input**

Reading text from the standard input stream (typically the keyboard).

**Standard Output**

Printing to the standard output stream (usually the console):

```python
print("hello!")\t# (will print with a newline)
print("hello!", end='')\t # (no newline)
```

**Static**

Belongs to the class itself, not to any individual instance. A static field is shared by all objects; a static method can be called without creating an object.

**String Concatenation**

Joining strings with `+` or a concatenation function: 

```python
"Hello" + " " + "World" → "Hello World"
" ".join("Hello", "World") → "Hello World"
```


**String Immutability**

Strings cannot be changed after creation. Operations on strings always produce a new string.

**Subtree**

A node and all of its descendants.

**`super()`**

Keyword Refers to the superclass. Used to call the superclass constructor (`super()`) or override methods (`super().method()`).

**Superclass / Subclass**

The parent class is the superclass; the child class is the subclass. The subclass inherits all non-private members of the superclass.

**Syntax**

The rules that define the structure and format of valid statements in a programming language. A syntax error means the code is grammatically wrong.

**Tail Recursion**

A recursive call that is the very last operation in the method. Some compilers/runtimes optimize this to avoid stack growth.

**Time Complexity**

A measure of how the runtime of an algorithm grows as the input size {math}`n` grows.

**Tree**

A hierarchical, acyclic data structure of nodes. One node is the root; every other node has exactly one parent.

**Variable**

A named storage location in memory that holds a value. Variables have a name, a type, and a value.

**`while`**

Repeats a block while a condition is true. Tests the condition before each iteration. May execute zero times.

