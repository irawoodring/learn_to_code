# Creating Our Own Types (Classes and Objects) 

Thus far, our programming style has been to create sequences of commands almost like a recipe for the computer to follow.  Originally that was the only way to communicate with computers - and at their core still is.  We call the model of programming where we give sequences of command **imperative** programming.  However, humans don't think that way.  Anyone who has tried to cook from a recipe has probably learned this truth the hard way - we often forget ingredients or miss steps.  The same thing happens when we try to build something from a set of instructions. In the 1960s, a computer scientest named Alan Kay theorized that the reason this happens is that humans don't naturally think in terms of processes.  We understand them, but the way we view and interact with our world is different.

Humans think in terms of objects.  We don't say, "I'm going to go to the room down the hall where the food is, grab a plate, bread, peanut butter, jelly, and a knife.  Then, I will open the jars and use the knife to put both subtances on the bread.  I will then...", so on and so forth.  Instead, we think, "I'm going to go make a PB&J."   We constantly think and speak about our world in terms of objects.  We talk about their **state** - the properties that define them, and their **behavior** - the things they are able to do.  For instance, we might talk about a truck being red and four-wheel drive, and that it can haul a load of a certain size.  Kay suggested that if we thought of code in the same way, that humans would make fewer mistakes when writing and maintaining it.

And thus, **Object-Oriented Programming** (OOP) was born.  Instead of writing long sequences of commands that share a bunch of variables, we create code objects that interact with one another and only have access to the variables they need to do their job.  We create a blueprint of an object by writing a **class**.  Then we create **instances** - objects built from the blueprint.

Python and many other languages let us make classes by using the `class` keyword:

```python
class Spaceship:
```

Notice that we usually always capitalize the name of the class - then when we see a capitalized word we know it is probably a data type and not a variable, method name, etc.  When an object is first made, we need to set up its default state.  Therefore, languages provide special methods called **constructors** to set things up the way we want them.  Python uses the name `__init__` to signify the constructor:

```python
class Spaceship:
  def __init__(self):
    ... setup code goes here ...
```

In our constructors we will define our **instance variables** (sometimes called fields or attributes).  Suppose we are coding a game that uses the `Spaceship` class we've started making here.  We might want to keep track of the name of each ship, the amount of health it has left, and perhaps a shield percentage.  So, we would create instance variables for each of these.  Note that an instance variable in Python must always start with the word `self`:

```python
class Spaceship:
  def __init__(self):
    self.name = "Default Name"
    self.hp = 1000
    self.shield = 1.0
```

We could then create instances of `Spaceship` by calling the constructor.  Notice that we call the constructor not with the name `__init__` but with the name of the class itself:

```python
falcon = Spaceship()
falcon.name = "Millennium Falcon"

firefly = Spaceship()
firefly.name = "Serenity"
```

Now we have two instances of the `Spaceship` class.  Each has a name, hp, and shield.  In the code above we changed each of the ship's names, but the other values stay the default values for now.  We use **dot notation** to access variables and methods for each instance, meaning we use the object's name, a dot (or period), then the name of the variable or method we wish to access.

## Encapsulation

We need to make a change to the way we created instance variables in the example above.  In many languages (particularly imperative ones), any part of the code has access to nearly all of the variables.  Imagine a car operating system that worked that way (and they exist!) - if any piece of code in the system could access any variable, the code that controls your lighting could access information in the braking system.  So, if a programmer made a simple mistake - perhaps using a variable name in the lighting system that was being used in the braking system, bad things could happen.  We want to prevent such situations from occurring.  Therefore, we use a principle called **encapsulation**.  We only give objects access to the data they need to do their job.  Then, we don't allow code from other types to access our data directly.  Instead, we provide methods to access and modify our data in the ways that we deem acceptable.

The problem with our code currently is that we have named our variables in such a way that other programmers will think it is **public** - available for any piece of code written by anyone to access and modify.  Many languages will require you to note whether a variable is public with a keyword; Python simply uses a naming convention.  The rules of the convention are:

- variables and methods named with two underscores in front of them, i.e. `self.__name` are **private** and should only be accessed by objects of that type.
- variables and methods named with a single underscore in front of them, `self.__name` are considered **protected**.   Protected means data should only be accessed and modified by objects of that type or one of their subtypes.  We will talk about subtypes in the chapter on inheritance.
- variables and methods named with no underscore are considered public.

For now, we are only going to talk about public and private variables and methods.  We are going to mark our data as private:

```python
class Spaceship:
  def __init__(self):
    self.__name = "Default Name"
    self.__hp = 1000
    self.__shield = 1.0
```

Now we need to provide methods to access our data.  Python provides two styles of methods - getters/setters, and properties.  They do the same things, but properties are easier to use.  We will illustrate each style in the sections that follow.

## Getters and Setters

A getter usually just returns a value.  If we don't want the values to be seen, we don't provide a getter.  They will typically be named with the `get_` and the variable name in Python:

```python
def get_name(self):
  return self.__name
```

If we want to allow our data to be changed, we can provide a setter.  They will be named (usually) `set_` and the name of our variable.  But here is where things can get tricky, as not every value a user passes in will be valid for our purposes.  For instance, for the `name`, we might want to have some criteria for what makes a valid name.  We want to make sure first and foremost that the user actually passed a string to us, and not a number or other type.  Python lets us check a type with the `isinstance()` function:

```python
def set_name(self, name):
  if not isinstance(name, str):
    raise TypeError("Name must be a string.") 
```

In languages that are **statically typed**, the types are usually checked by the programming language before the program is run.  Python is a **dynamically typed** language, meaning types are assigned to variables when we use them - i.e. when the program is running.  Therefore we need to check the types ourselves.

But, we still aren't done.  Just because we got a string doesn't mean we got a valid string.  We probably don't want an empty string - "" as a ship name.  We also may not want a name that is too long.  For our purposes, let's say that a ship name must be between 3 and 20 characters long.  To ensure that is the case, we will check the value passed into our setter to ensure it is ok before we accept it:

```python
def set_name(self, name):
  if not isinstance(name, str):
    raise TypeError("Name must be a string.")
  if len(name) < 3 or len(name) > 25:
    raise ValueError("Name must be between 3 and 20 characters.")
  self.__name = name
```

A few things to note here - we tested type *before* we tested value.  If we had tried to test the length first, and the user had passed in a number, the program could have crashed because you can't get the length of a number (it isn't a collection).  Always test type before you test values.  We raised exceptions of the appropriate kind if our rules were violated - a `TypeError` if `name` wasn't a string, and a `ValueError` otherwise.  And we raised them with appropriate messages.  Finally, we only changed our private data to the value passed into the method if all of our tests passed.  This is encapsulation in a nutshell - we've wrapped access to our data behind methods that understand how to work on it safely.  We want to make sure that the rules for our data are never violated.

## Properties

There is nothing inherently wrong with getters and setters.  However, calling them can get cumbersome and a bit verbose.  Imagine we rewrote our constructor function to take parameters:

```python
class Spaceship:
  def __init__(self, name="Default Name", hp=1000, shield=1.0):
```

This would make it easier for users to create new instances of the `Spaceship` class.  But now, since users can pass values into the constructor, we need to validate the data they send.  So we need to call our setters, since that is where the code that validates our data is stored:

```python
class Spaceship:
  def __init__(self, name="Default Name", hp=1000, shield=1.0):
    self.set_name(name)
    self.set_hp(hp)
    self.set_shield(shield)
```

This code can be a bit confusing.  For one thing, it doesn't make clear that we are creating instance variables in our constructor.  True, a user could look up each function and see that that is what is happening - but there is no context clue in this local piece of code that shows we are setting a value.  Secondly, the three lines all start with the string `self.set_`, which can be a bit confusing for our brains to look at and decode.  Some languages (like Python), give us a different way of doing the same thing, but with an easier to read syntax.  We call these **properties**.  A property is a way to define an attribute on a class that runs a method behind the scenes when you read or write it, while still looking like a plain attribute (instance variable) to the caller.

We define a read property with the `@property` annotation:

```python
@property
def name(self):
  return self.__name
```

You may notice that other than the annotation, that the only thing that changed was the signature get_name(self)` became `name`.  But now, we can read the value of `self.__name` as if it were a public variable.  For instance, if we had still had our ship named `falcon`, we could write:

```python
print(falcon.name)
```

And `Millennium Falcon` would print.  We can similarly create a setter to add write access to our variable:

```python
@name.setter
def name(self, name):
  if not isinstance(name, str):
    raise TypeError("Name must be a string.")
  if len(name) < 3 or len(name) > 25:
    raise ValueError("Name must be between 3 and 20 characters.")
  self.__name = name
```

Again, the only parts that changed are the annotation and method signature.  The validation code is all still the same.  Our annotation must be of the form `<PROPERTY_NAME>.setter`.  Now, we can write to `self.__name` as if it were a public variable:

```python
self.name = "Falcon"
```

This will automatically call our setter code to ensure that the value on the right of the equals sign was valid.  Once all three properties are written, we can rewrite our constructor:

```python
class Spaceship:
  def __init__(self, name="Default Ship", hp=1000, shield=1.0):
    self.name = name
    self.hp = hp
    self.shield = shield
```

This code is much cleaner and takes less time to write.  Further, we are using variable assignment syntax, so we've provided a context clue that our code is creating instance variables.  Overall, this code should be easier to read and maintain.

## Dunder Methods

There are a lot of commong operations we might wish to perform on objects.  We may wish to print out a human-readable representation of them, for instance.  Or compare two objects of the same type in some way.  For the `Spaceship`, that might be checking to see if the `hp` of one is larger or smaller than another when they are attacking, or to sort a collection of ships by one of their attributes.  Python has quite a few of these special purpose methods.  When you make an object, you might get default versions of some of these methods.  For instance, if we use `dir()` on an instance of `Spaceship`, you will see output similar to this:

```python
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__',
'__weakref__'
```

Notice how each of these methods start and end with double underscores?  Because of this, we call them **dunder** (double underscore) methods.  We won't go into what all of them do here.  Instead, we will list the more commonly used ones.  Those are usually:

- `__bool__` - Defines the truthiness of an object, called by bool() and evaluated in any boolean context such as `if ship:`, `while ship:`, or `not ship`. Should always return `True` or `False`.  If `__bool__` is not defined, Python falls back to `__len__` (the object is `False` if its length is 0). If neither is defined, all instances of the class are considered `True` by default.
- `__eq__` - Defines behavior for the `==` operator. Without it, Python defaults to identity comparison, meaning two variables are only considered equal if they point to the exact same object in memory. By defining `__eq__`, you can instead compare objects by their attribute values, so two separate instances with the same data will evaluate as equal.
- `__ge__` - Defines behavior for the `>=` (greater than or equal to) operator.
- `__hash__` - Defines the integer hash value returned by `hash()`. Required for objects to be usable as dictionary keys or set members. Critically, Python's rule is that objects that compare equal must have the same hash. If you define `__eq__`, Python will set `__hash__` to `None` (making the object unhashable) unless you also explicitly define `__hash__`.
- `__le__` - Defines behavior for the `<=` (less than or equal to) operator.
- `__lt__` - Defines behavior for the `<` (less than) operator. Also used by `sorted()` and `min()`/`max()` when no key is provided, making it the most important comparison dunder to implement if you want sortable objects.
- `__ne__` - Defines behavior for the `!=` operator. By default Python automatically derives it as the inverse of `__eq__`, but you can override it for custom not-equal logic.
- `__repr__` - Defines the "official" or developer-facing string representation. Called by `repr()` and shown in the REPL. The goal is an unambiguous string, ideally one that could be copy-pasted to reconstruct the object. If `__str__` is not defined, Python falls back to `__repr__`.
- `__str__` - Defines the "informal" or human-readable string representation of an object. Called by `print()` and `str()`.

Let's create these now, and finish up the `Spaceship` class!

## Finishing Up the Spaceship Class

Here is a final version of the `Spaceship` class, commented according to Google's Python Style Guide:

```python
"""Module for representing a Spaceship with validated attributes."""


class Spaceship:
    """Represents a spaceship with a name, health points, and shield level.

    Attributes:
        name: A non-empty string of 3–20 characters identifying the ship.
        hp: Hull points representing remaining structural integrity; must
            be a positive integer.
        shield: Shield strength expressed as a percentage fraction
            between 0.0 (no shields) and 1.0 (full shields).

    Example:
        >>> ship = Spaceship(name="Avalon", hp=500, shield=0.75)
        >>> print(ship)
        Spaceship | Name: 'Avalon' | HP: 500 | Shield: 75.0%
        >>> ship.hp -= 100
        >>> ship.shield = 0.5
        >>> print(ship)
        Spaceship | Name: 'Avalon' | HP: 400 | Shield: 50.0%
    """

    MIN_NAME_LEN = 3
    MAX_NAME_LEN = 20
    MIN_SHIELD = 0.0
    MAX_SHIELD = 1.0

    def __init__(self, name: str, hp: int, shield: float) -> None:
        """Initializes Spaceship with validated attributes.

        Args:
            name: A non-empty string between 3 and 20 characters.
            hp: Hull points; must be a positive integer.
            shield: Shield percentage as a float between 0.0 and 1.0.

        Raises:
            TypeError: If any argument is of the wrong type.
            ValueError: If any argument fails its validation check.
        """
        self.name = name
        self.hp = hp
        self.shield = shield

    # --- name property -------------------------------------------------

    @property
    def name(self) -> str:
        """str: The name of the spaceship (3–20 characters)."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f"name must be a str, got {type(value).__name__}."
            )
        stripped = value.strip()
        if not stripped:
            raise ValueError("name cannot be empty or whitespace.")
        if not (self.MIN_NAME_LEN <= len(stripped) <= self.MAX_NAME_LEN):
            raise ValueError(
                f"name must be between {self.MIN_NAME_LEN} and "
                f"{self.MAX_NAME_LEN} characters, got {len(stripped)}."
            )
        self.__name = stripped

    # --- hp property --------------------------------------------------

    @property
    def hp(self) -> int:
        """int: Hull points; reflects remaining structural integrity."""
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(
                f"hp must be an int, got {type(value).__name__}."
            )
        if value <= 0:
            raise ValueError(f"hp must be a positive integer, got {value}.")
        self.__hp = value

    # --- shield property -----------------------------------------------------

    @property
    def shield(self) -> float:
        """float: Shield strength as a fraction between 0.0 and 1.0."""
        return self.__shield

    @shield.setter
    def shield(self, value: float) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"shield must be a float, got {type(value).__name__}."
            )
        value = float(value)
        if not (self.MIN_SHIELD <= value <= self.MAX_SHIELD):
            raise ValueError(
                f"shield must be between {self.MIN_SHIELD} and "
                f"{self.MAX_SHIELD}, got {value}."
            )
        self.__shield = value

    # --- Dunder Methods -----------------------------------------------------

    def __str__(self) -> str:
        """Returns a human-readable summary of the spaceship.

        Returns:
            A formatted string showing name, HP, and shield percentage.
        """
        return (
            f"Spaceship | Name: '{self.__name}' | "
            f"HP: {self.__hp} | "
            f"Shield: {self.__shield * 100:.1f}%"
        )

    def __repr__(self) -> str:
        """Returns an unambiguous developer-facing representation.

        Returns:
            A string from which an equivalent Spaceship can be reconstructed.
        """
        return (
            f"Spaceship("
            f"name={self.__name!r}, "
            f"hp={self.__hp!r}, "
            f"shield={self.__shield!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Checks equality based on all three core attributes.

        Args:
            other: The object to compare against.

        Returns:
            True if other is a Spaceship with identical name, hp, and
            shield; False otherwise.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return (
            self.__name == other.__name
            and self.__hp == other.__hp
            and self.__shield == other.__shield
        )

    def __lt__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (ascending).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has fewer HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp < other.__hp

    def __le__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (less than or equal).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has fewer or equal HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp <= other.__hp

    def __gt__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (greater than).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has more HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp > other.__hp

    def __ge__(self, other: "Spaceship") -> bool:
        """Compares spaceships by HP (greater than or equal).

        Args:
            other: The Spaceship to compare against.

        Returns:
            True if this ship has more or equal HP than other.

        Raises:
            TypeError: If other is not a Spaceship.
        """
        if not isinstance(other, Spaceship):
            return NotImplemented
        return self.__hp >= other.__hp

    def __bool__(self) -> bool:
        """Evaluates the ship's operational status.

        Returns:
            True if the ship has positive HP and any shield remaining;
            False if shields are fully depleted.
        """
        return self.__shield > self.MIN_SHIELD

    def __hash__(self) -> int:
        """Returns a hash based on the ship's name, HP, and shield level.

        Returns:
            An integer hash value.
        """
        return hash((self.__name, self.__hp, self.__shield))

```


## Using the `Spaceship` Class

Now that we have a complete `Spaceship` class, let's see how we can use it. Recall from earlier in this chapter that we call the constructor by using the class name.  Now that we have a constructor that can take parameters, we will pass the values we wish to use for the class in the call: 

```python
firefly = Spaceship("Serenity", 1000, 1.0)
falcon = Spaceship("Millennium Falcon", 750, 1.0)
enterprise = Spaceship("Enterprise", 1500, 1.0)
```

Printing each of these results in the output:

```python
Spaceship | Name: 'Serenity' | HP: 1000 | Shield: 100.0%
Spaceship | Name: 'Millennium Falcon' | HP: 750 | Shield: 100.0%
Spaceship | Name: 'Enterprise' | HP: 1500 | Shield: 100.0%
```

While the `__repr__` for each would output:

```python
"Spaceship(name='Serenity', hp=1000, shield=1.0)"
"Spaceship(name='Millennium Falcon', hp=750, shield=1.0)"
"Spaceship(name='Enterprise', hp=1500, shield=1.0)"
```

Our comparison operators work as well.  We won't print the output from every possible comparison, but here are a few comparisons and what they result with:

```python
firefly > falcon		# True
enterprise < firefly		# False
enterprise == falcon		# False
falcon == falcon		# True
firefly != falcon		# True
falcon <= firefly		# True
```

We can even hash our objects, which allows us to use them as dictionary keys (among other uses):

```python
hash(firefly)			# -5220248866166253478
hash(falcon)			# 6271764174197419405
hash(enterprise)		# 7382750676208440033
```

Note that your hashes may not be the same as mine - that's ok and normal Python behavior!

## Final Thoughts

You may not always need as complete a class as we presented here.  And, sometimes you might need one that has even more behavior.  The `Spaceship` class is just an example of what you can do, and how you can do it.

Moving forward, we will learn how classes interact with one another, and how we can create new classes by customizing existing ones - without rewriting the entire class.
