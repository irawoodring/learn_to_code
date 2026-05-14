# Chapter 3 - Collection Type Variables

Sometimes we want to group values together and refer to the group with a name.  For instance, we might have a list of groceries we need to pickup at the store, or a group of phone numbers organized by name.  Python provides several built-in types that allow us to keep groups of values together.  These types are broken up into three categories - sequence types, mapping types, and set types.

```{table} Python Collection Types
:name: python-collection-types
| Type | Description | Example | Category |
|:-----|:------------|:--------|:---------|
| `list` | Mutable ordered sequence | `[1, 2, 3]` | **Sequence** |
| `str` | Immutable sequence of Unicode characters | `"hello"` | **Sequence** |
| `tuple` | Immutable ordered sequence | `(1, 2, 3)` | **Sequence** |
| `range` | Immutable sequence of integers | `range(0, 10)` | **Sequence** |
| `dict` | Mutable key-value pairs | `{"a": 1}` | **Mapping** |
| `set` | Mutable unordered collection of unique items | `{1, 2, 3}` | **Set** |
| `frozenset` | Immutable unordered collection of unique items | `frozenset({1, 2})` | **Set** |
```

## Sequence Types

A sequence type is a collection where each value is given an index number.  The number helps us to know which value in the collection we are trying to refer to.  Sequence types allow us to use the **indice operators** '[]' to specify which index's data we wish to access.  We will show examples of using the indice operators in the sections that follow.

### list

The `list` type is the workhorse of Python collections.  We can create a list in multple ways:

```python
groceries = []
votes = list()
my_grades = [97.8, 93.0, 95.5, 87.9]
```

The first method is generally preferred, and is really just a shortcut for the second.  Both the first and second method create empty lists that we can then add to later.  The third method creates a list with values already added.

We can always change lists once they are created.  You may have noticed in the table above that we used the words **mutable** and **immutable**.  Mutable simply means that a variable can change once created.  Immutable means that once created, the values are fixed.  Whether you use a mutable or immutable data type depends a lot on the problem you are trying to solve.  Lists are mutable.

So how do we work with information in a list?  As we mentioned above, with sequence types you can use the indice operators - `[]`.  So, if we wanted to access the first element from our `my_grades` list from above, we would write:

```python
my_grades[0]
```

or, to change the value to a new value:

```python
my_grades[0] = 99.9
```

Python provides the `len()` function to determine the length, or number of elements, in a list:

```python
print(len(my_grades))
```

would output `4`.  Notice that indexes in Python are **zero-based indexes**, meaning they start at 0 instead of 1.  This means that our `my_grades` list has indexes 0, 1, 2, and 3 - and no index 4.  Trying to access an element 4 would result in `IndexError: list index out of range` being printed on the console (or raised as an exception if this line were in a program).  You can practice working with lists in the box below; it is a Python implementation that runs in your browser, on your computer.  Don't worry about messing anything up - you can just refresh the page to start over! 

<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1&code=groceries%20%3D%20%5B%5D%0Avotes%20%3D%20list%28%29%0Amy_grades%20%3D%20%5B97.8%2C%2093.0%2C%2095.5%2C%2087.9%5D%0A""
  width="100%"
  height="100%"
></iframe>

We will have a full chapter on working with lists, as well as some sample code using a list to solve a problem.  In that chapter we will go over many of the built-in Python lists functions that make working with lists easier.

## str

Strings may not seem like a collection, but really they are.  They are simply a list of characters.  We use strings anytime we need to get information from or present information to the user.  Strings are a sequence type, as each character has an index and we can use all of the same indice operators as lists on strings.  Creating a string is simple, just surround your text with quotes.  Python doesn't care if you use single-quotes `'` or double quotes `"`, but a string has to be started and ended with the same quote type.  All of the following are valid Python strings:

```python
name = 'Mr. W'
course = "CS1"
message = f"Hi, my name is {name} and I teach {course}."
string_with_quote = "I can't stand bananas."
escaped_quote = "I said, \"Why, hello there.\""
```

The third style string is called an **f-string**.  These are formatted strings.  We can use an f-string anywhere we can use a normal string.  An f-string must start with an 'f'.  We can include a variable or other Python expression inside of the curly braces, and the output will be added to the string.  The above f-string results in "My name is Mr. W and I teach CS1."  We often use f-strings when we want to embed the value from a variable into a string.  It is much easier that converting a value to a string and then combining the strings together manually.

The fourth string, `string_with_quote`, shows how we can embed a quote inside of a string.  Here we put a single quote inside of a string composed with double quotes, but we could do the opposite as well.  The string `escaped_quote` shows how we can embed a quote of one type inside of a string that is started and ended with that same type.  In this case, we **escape** the character we wish to embed - in this example the `"` - by placing a backslash "\" before it.


