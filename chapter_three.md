# Chapter 3 - Collection Types

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



