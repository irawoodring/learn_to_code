# Object-Oriented Programming

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
- variables and methods named with a single underscore in front of them, `self._name` are considered **protected**.   Protected means data should only be accessed and modified by objects of that type or one of their subtypes.  We will talk about subtypes in the chapter on inheritance.
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


