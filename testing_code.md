# Testing Code

In the chapter "Creating Our Own Types", we introduced the `Spaceship` class.  We noted that it held three pieces of data:

- `name`: A non-empty string of 3–20 characters identifying the ship.
- `hp`: Health points representing remaining structural integrity; must be a positive integer.
- `shield`: Shield strength expressed as a percentage fraction
            between 0.0 (no shields) and 1.0 (full shields). 

:::{dropdown} Click here if you wish to view the `spaceship.py` file.
:::{literalinclude} code_samples/spaceship.py
:linenos: 
:language: python
:::

So once we have some code, whether it came from a junior developer, an LLM, or even ourselves, how do we know it works?  This is where testing comes into play.  Testing software is one of the most essential parts of creating software - and one that many folks overlook.  Testing is sometimes seen as "not fun", or tedious.  We need to break away from that mindset.

But testing software can be really fun.  It gives us a chance to play as the hacker, to think about how the code is supposed to operate and to try to trick it into doing something different.  It is a role we don't often get to play because of legal and ethical issues - but in the context of testing software it is a good thing!

How do we test software though?  The most basic way is with **unit tests**.  A unit test is a piece of code that attempts to test one tiny part of your program - often a function or part of a function.  Unit tests are usually small, fast, independent of other tests, and should always give the same result back.  For instance, suppose we have a class called `Color`.  Computers often store colors as a collection of red, green, and blue light values that mix together to make the color.  Often these values can only be between 0 and 255.  Suppose we had a method `set_red(self, red)`.  Our unit test process might look like this:

- Create a new instance of `Color`
- Check that the current value of `red` is whatever our starting value should be (for our purposes we will say 0)
- Call the method with valid values and check that `red` changed accordingly
- Call the method with invalid values and check that `red` didn't change (or more likely that it threw an exception

If any of our checks result in a value we don't expect, then the test fails and we say the method is broken.  Python has multiple unit testing libraries available; we will use Pytest for our examples.  Here is how we might write our tests for the `red` setter:

```python
import pytest

# First, we will test sample values that *should* be accepted
@pytest.mark.parametrize("value", [0, 1, 127, 254, 255])
def test_red_setter_valid_values(value):
    color = Color()

    color.red = value

    assert color.red == value


# Now, test some samples that *should not* be accepted
@pytest.mark.parametrize("value", [-1, 256, 'hello', 4.56, True, None])
def test_red_setter_invalid_values(value):
    color = Color()

    with pytest.raises(ValueError):
        color.red = value
```

The code we are using makes use of **parameters** for testing.  For each of the values in our valid and invalid list, the test will be called and run.  Our fist set of tests use the `assert` statement; an **assertion** is something that must be `True` or the test fails.  In our `test_setter_valid_values` tests, we create a new `Color`, set its value to whichever valid value was passed in for that instance of the test, and then we assert - or insist - that the value stored in `red` is the one we gave it.

In our second testing function, we are still asserting, but more indirectly.  Here, we are saying that we are going to provide an invalid value and that our could *should* raise a `ValueError`.  If it does not, then our test fails.

Notice that we didn't pass every possible valid integer in the first test.  In this example we could have - running 256 different values wouldn't take that long - but often time constraints will prevent us from doing so.  For our invalid values tests we didn't test every possible invalid integer (there are an infinite number of them!).  We also passed values that are **not** integers; in this case we passed a string, a float, a boolean, and even a `None`.  We expect each of those to result in a `ValueError` being raised by the `Color` instance. 

:::{dropdown} Click here if you wish to view the `test_spaceship.py` file.
:::{literalinclude} code_samples/test_spaceship.py
:linenos: 
:language: python
:::

