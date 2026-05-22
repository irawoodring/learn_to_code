# An Introduction to Variables

As mentioned in the last chapter, computers store data in their memory.  At its deepest level, memory is just electricity in circuits.  While not entirely true, we can think of memory as being made up of many locations, with each location able to either be empty or store electricity.  We tend to call these locations **bits** which is a shortening of the words for "binary digit".  We usually think of a location storing no electricity as holding a '0' and a location with electricity as holding a '1'.  Again, this is an oversimplification, but it works to help us build a mental model of how memory works.

A single bit on its own isn't very useful, so typically computers group them together to form **bytes**.  Often, a byte is eight bits - but not always.  The size of a byte for any system will typically be decided upon by the engineers designing a CPU.  Every byte on a system will have an **address** - that is, a number that tells the computer its location.

Numbers are great for computers, but not so great for people.  We don't, for instance, refer to each other by our Social Security numbers.  Humans are much better with names.  Programming languages thus allow us to give a name to a memory location so that we can easily refer to it.  We call these named locations **variables**.  Every language will have rules for how a variable can be named.  In Python, the rules are:

- variables can only be made from letters a-z, A-Z, digits 0-9, and the underscore '_'.
- they cannot start with a digit
- a variable name is case sensitive - my_variable is different than My_Variable, or my_Variable, or even mY_vArIaBlE.
- Python keywords may not be variable names.  These include

	```{table} Python Reserved Keywords
	:name: python-keywords

	| Category | Keywords | Purpose |
	|:---------|:---------|:--------|
	| **Boolean / Null literals** | `True` `False` `None` | Built-in constant values |
	| **Boolean operators** | `and` `or` `not` | Logical operations |
	| **Conditional** | `if` `elif` `else` | Branching logic |
	| **Loops** | `for` `while` `break` `continue` | Iteration and loop control |
	| **Functions** | `def` `return` `lambda` `yield` | Define and return from callables |
	| **Classes** | `class` `del` | Define and destroy objects |
	| **Exception handling** | `try` `except` `raise` `finally` | Error handling |
	| **Context managers** | `with` `as` | Resource management |
	| **Imports** | `import` `from` `as` | Load modules |
	| **Scope** | `global` `nonlocal` | Variable scope declaration |
	| **Identity / membership** | `is` `in` | Object identity and containment tests |
	| **Async** | `async` `await` | Asynchronous execution |
	| **Miscellaneous** | `pass` `assert` | No-op placeholder; debugging assertion |
	```

Since variables are just made out of bits, we need a way to tell the computer how we want those bits interpreted.  After all, the bits could be used to represent a number, a character, another memory address, or a host of other things.  We call how a variable is interpreted its **type**.  The types that Python come with are:

```{table} Python Built-in Types
:name: python-builtin-types

| Type | Description | Example |
|:-----|:------------|:--------|:---------|
| `int` | Integer of unlimited precision | `42`, `-7`, `0` |
| `float` | IEEE 754 double-precision float | `3.14`, `-0.5` |
| `complex` | Complex number with real and imaginary parts | `3+4j` |
| `bool` | Boolean subclass of `int` | `True`, `False` |
```

Now, I know there are some words in this table that might be confusing, so we will go over each type in the sections below, along with some examples of how to create a variable of that type.  To simplify things, we will organize the following sections by category.  A category of variables are similar in some ways.

## Python's Numeric Types 

A numeric variable simply holds a number.  As there are different types of numbers, we need different types of variables to hold them.  You've probably learned in your math courses about different number types such as integers, real numbers, complex numbers, etc.  Python is the much the same.  Python also give us the math operators you'd expect.  For example:

```{table} Math Operators for Numeric Types
:name: python-math-operators

| Operator | Name | Example | Output |
|:---------|:-----|:--------|:------|
| + | Addition | 3 + 2 | 5 |
| - | Subtraction | 5 - 1 | 4 |
| * | Multiplication | 7 * 6 | 42 |
| / | Division | 10 / 3 | Output for this will look like 3.3333333333333335.  Notice we don't have unlimited precision for non-integers. |
| // | Integer Division | 10 // 3 | Output for this will be 3.  Integer division only gives you the whole-number part of a division operation. |
| % | Modulo | 10 % 3 | Modulo simply gives the remainder.  If we divide 10 by 3, we have 1 left over - that would be the output from modulo. |
| ** | Exponentiation | 2 ** 3 | This would raise 2 to the 3rd power, resulting in 2 * 2 * 2 = 8.|
```

Python also allows us to writeout more complicated expressions such as `(3 * 10) + (6 // 2)` which would output `33`.

### int

An `int` is simply an integer, or whole number.  It can be positive, negative, or zero.  Python allows for **unlimited precision** for integers; this means that our numbers can get arbitrarily large or small.  We can create integers as such:

```python
my_integer = 42
number = 1701
```

And can use them in other expressions as well:

```python
length = 10
width = 5
area = length * width
print(area)
```

Which would output `50`. 

### float

A `float` is a whole number, a decimal point, and a fractional part.  We saw the result of `10 / 3` was `3.3333333333333335`.  You might have expected a value more like `3.\overline{3}`.  This is, after all, how we would write it in math class.  However, since computers are storing these values as bits, and we have a limited number of bits, we have to cut things off somewhere.  This is why we get the odd looking `5` at the end.  Computers can rarely be exact when performing **floating-point math** - that is math with floats.  Therefore, we always need to be careful if we are performing a calculation that requires high-precision, such as a scientific calculation or a calculation with money.

Some examples of creating and working with floats are:

```python
pi = 3.14159
radius = 12.2
area = pi * radius
print(area)
```

Which would result in the value `38.327397999999995` being printed.

### complex

Complex numbers (you may remember from a prior math course) are numbers composed of two parts - a real part and an imaginary part.  We represent the real part in Python just as we do any other number.  For the imaginary part, we simply add a `j` after it.  For instance:


```python
3 + 2j
6 - 3j
```

This may be confusing to some, as we often learn in math courses that an imaginary number makes use of {math}`i=\sqrt{-1}`.  Therefore, we often write our complex numbers as {math}`3 + 2i`.  Electrical engineers use `j` instead of `i` to avoid confusion, and Python chose to do the same.

### bool

A `bool` or Boolean is a variable type that only holds one of two values - either `True` or `False`.  You might be thinking this is a weird type to include in the "Numeric" category, but hopefully it will make sense after a bit of explanation.  In Python (and many other languages), `0` is used to represent `False`.  Anything other than `0` is used to represent `True`.  While this may seem as if it makes no sense, remember that all values need to be stored in variables as bits composed of 0s and 1s.  When programmers back in the day wanted to use bits to represent true and false values, they chose all 0s to represent `False`, and it has stuck to this day.

Further, in Python every variable has a **truthiness**.  The values

- None
- Zero of any numeric type: 0, 0.0, 0j
- Empty sequences and collections: "", [], (), {}, set()
- Empty range: range(0)
- Objects who have a ` __bool__` method that returns `False` or `__len__` method that returns 0

are all considered `False`.  Any other values are `True`.  This allows us to use some nice shortcuts in our `if` statements (I know you haven't seen an `if` statement in this text yet, but we will get there shortly!).  For instance, if we want to see if a string is empty, instead of running the code:

```python
if len(my_string) == 0:
  ... do something ...
```

we can use a much shorter form:

```python
if not my_string:
  ...  do something ...
```

Python (and many other languages) include little shortcuts like these that make it easier and quicker to write programs.  You will pick them up as you progress in your programming knowledge.

Creating a `bool` is also easy:

```python
is_finished = True
game_over = False
size = 5
is_bigger = size < 12
```

The first two are self-explanatory - just remember that Python requires `True` and `False` to be capitalized.  The third example is creating a boolean by way of a comparison operator.  Since `5 < 12`, the value for `is_bigger` will be `True`.  We will use comparators a lot when we get to `if` statements.  For now, just keep in mind they exist.
