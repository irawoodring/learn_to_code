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

- variables and methods named with two underscores in front of them, i.e. `self.__name`` are **private** and should only be accessed by objects of that type.
- variables and methods named with a single underscore in front of them, `self._name` are considered **protected**.   Protected means data should only be accessed and modified by objects of that type or one of their subtypes.  We will talk about subtypes in the chapter on inheritance.
- variables and methods named with no underscore are considered public.

For now, we are only going to talk about public and private variables and methods.
