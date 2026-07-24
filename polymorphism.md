# Polymorphism in Python
 
Polymorphism is a word which is derived from the Greek poly (many) and morph (forms), and is a fundamental pillar of Object-Oriented Programming (OOP). In software engineering, it refers to the ability of different types to be treated as instances of a common group type, where each individual type provides its own specific implementation for a shared method.
 
In Python, polymorphism is baked into the language's dynamic nature, in a few different ways. This chapter explores the spectrum of polymorphism in Python, from informal "Duck Typing," to formal Abstract Base Classes (ABCs), and finally to Structural Typing via Protocols (a feature added after Python 3.8). 
 
## First things first - Inheritance vs. Polymorphism 
 
It is important that we first distinguish between these two often-confused terms: 
- Inheritance is a mechanism for structure. It allows a class (such as a Dog) to inherit the attributes and methods of another class (Animal). It answers the question: "What is this object?" 
- Polymorphism is a mechanism for behavioral consistency. It allows different objects (a Dog, a Cat, and a Bird) to be treated as "Animals" when we only care that they can, for instance `.make_sound()`. It answers the question: "What can this object do?" 
 
A polymorphic system ensures that even if the underlying implementation of make_sound() differs for every species, the caller (the code executing the sound) remains unchanged. 

## Duck Typing: Informal Polymorphism

Python is famous for Duck Typing. This philosophy states: "If it walks like a duck and quacks like a duck, then it must be a duck." 
 
In a duck-typed system, the interpreter doesn't care about the type of an object; it only cares if that object supports the method being called at runtime. 
 
```python 
class Person: 
  def speak(self): 
    print("Hello there!") 
 
class Robot: 
  def speak(self): 
    print("Beep Boop. I am speaking.") 
 
def activate_speech(entity): 
  # This function is polymorphic because it works with any object 
  # that has a .speak() method. 
  entity.speak() 
 
activate_speech(Person()) 
activate_speech(Robot()) 
``` 
 
### Advantages of Duck Typing: 
 
- Maximum Flexibility: You can swap out components easily without complex inheritance hierarchies. 
- Simplicity: It is often the easiest way to write code that interacts with third-party libraries. 
 
### Disadvantages of Duck Typing: 
 
- Runtime Errors: If you pass an object that doesn't have the method, the program crashes only when it hits that line (AttributeError). 
- Lack of Discoverability: It’s harder for IDEs and static analysis tools to provide accurate autocomplete or type checking. 
 
## Abstract Base Classes (ABCs): Formalizing Interfaces 
 
As applications scale, relying solely on "trust" (Duck Typing) becomes dangerous. We need a way to guarantee that an object conforms to a specific contract before we try to use it. This is where Abstract Base
Classes (ABCs) come in. 
 
An ABC defines a blueprint. If a class inherits from an ABC but fails to implement one of the @abstractmethod decorators, Python will refuse to instantiate that class. 
 
```python 
from abc import ABC, abstractmethod 
 
class Flyer(ABC): 
  @abstractmethod 
  def fly(self): 
  """All flyers must implement this method.""" 
    pass 
 
class Airplane(Flyer): 
  def fly(self): 
    print("Engines engaged. Taking off.") 
 
class Bird(Flyer): 
  def fly(self): 
    print("Flapping wings.") 
 
# This will raise a TypeError: 
# Can't instantiate abstract class StaticObject with abstract method fly 
# class StaticObject(Flyer): 
# pass 
# obj = StaticObject() 
``` 
 
### When to use ABCs: 
 
- Enforcing Rules: When you want to ensure that developers must implement certain methods. 
- Shared Logic: Unlike Protocols, ABCs can also provide default implementations or shared state (like a __init__ method). 
- Clear Hierarchy: When the "is-a" relationship is meaningful for your domain model. 
 
## Structural Typing with Protocols (Static Duck Typing) 
 
Introduced in Python 3.8 (PEP 544), typing.Protocol provides a way to achieve structural typing—the closest equivalent to interfaces found in languages like Go or TypeScript, but within Python's type system. 
 
While an ABC requires you to inherit from the class (class Airplane(Flyer)), a Protocol only requires that your class matches the structure of the protocol. You do not need to inherit from anything. 
 
```python 
from typing import Protocol 
 
class Drawable(Protocol): 
  def draw(self) -> None: 
    ... 
 
class Circle: 
  def draw(self) -> None: 
    print("Drawing a circle.") 
 
class Square: 
  def draw(self) -> None: 
    print("Drawing a square.") 
 
  def render_shapes(shapes: list[Drawable]): 
    for shape in shapes: 
      shape.draw() 
 
# Circle and Square do NOT inherit from Drawable, 
# but they satisfy the Protocol because they possess a .draw() method. 
render_shapes([Circle(), Square()]) 
``` 
 
### Why Protocols are superior for many cases: 
 
- Non-Invasive: You can make a class compatible with a protocol without modifying its source code (perfect for third-party types). 
- Static Analysis: They work beautifully with tools like mypy to catch errors before the code runs. 
- Purely Structural: It describes what an object looks like, not what it is. 
 
# Comparison: ABC vs. Protocol 
 
| Feature     | Abstract Base Classes (ABC)           | Protocols (Structural Typing)                      |
|-------------|----------------------------------------|-----------------------------------------------------|
| Requirement | Explicit inheritance (class A(Base))  | Implicit implementation (Matches structure)        |
| Enforcement | Runtime (Instantiation check)         | Static (Type checker) & Runtime (Dynamic)          |
| State/Logic | Can hold state and concrete methods   | Generally for structural definitions only          |
| Use Case    | "Is-A" relationships, shared behavior | "Can-Do" capabilities, cross-library compatibility |
 
## Polymorphism in the Standard Library 
 
The best example of polymorphism in Python is its own built-in functions. Consider len(): 
 
```python 
 len([1, 2]) # Works on List 
 len("Hello") # Works on String 
 len({1, 2, 3}) # Works on Set 
 len(range(10)) # Works on Range 
``` 
 
How does len() know how to handle these? It uses polymorphism! Every object that implements the `__len__` method is considered "compatible" with the `len()` function. Another way of putting it is, any object with a `__len__` method can quack like that duck! This allows one function to work across infinite types without knowing anything about their internal implementation details. 
 
# The Liskov Substitution Principle (LSP) 
 
When designing polymorphic systems, you should adhere to the **Liskov Substitution Principle**. Barbara Liskov developed this principle.  It states that if a program is written to use objects of type A, it should still work perfectly fine if you replace those objects with instances of subclass B.
 
A common violation of LSP occurs when a developer creates a subclass but changes its behavior so much that it breaks existing logic. For example, a `Penguin` class inheriting from `Flyer` but raising an error on `.fly()` violates the contract established by the `Flyer` supertype. To maintain polymorphic integrity, subclasses must honor the promises made by their parents. A more nuanced (but classic) example is with `Rectangle` and `Square` classes.  Consider:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # forces height to match width

    def set_height(self, height):
        self.width = height
        self.height = height  # forces width to match height
```

This seems ok at first - after all a square *is* a rectangle mathematically.  But, it breaks the LSP because `Square` changes the behavior that code relying on `Rectangle` expects.  If we later used the code:

```python
def test_rectangle_area(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(4)
    assert rect.area() == 20  # this is a reasonable expectation for any Rectangle
```

And we pass in a `Square`, setting the height will silently overwrite the width.  That's not how a `Rectangle` works!  Therefore, we have violated the behavioral contract that `Rectangle` established - in this case that width and height could be set separately.  A better way of writing the above could be:

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
"""

Now there is no expectation that `Square` act like a `Rectangle`.

# Design Strategy: Composition Over Inheritance 
 
While polymorphism is often taught through inheritance hierarchies, modern Python developers often prefer Composition. Instead of creating a complex hierarchy for every possibility (e.g., `FlyingCar`, `DrivingCar`), you can build objects that contain other objects. For instance:
 
```python 
class Engine: 
  def start(self): 
    pass 
 
class ElectricEngine(Engine): 
  def start(self): 
    print("Silent power engaged.") 
 
class Car: 
  def __init__(self, engine: Engine): 
    self.engine = engine # Compositional approach 
 
def start_car(self): 
  self.engine.start() 
 
# We use polymorphism here to swap out the engine type 
# without changing the Car class structure. 
my_car = Car(ElectricEngine()) 
my_car.start_car() 
``` 
 
# When to Use Each Method?
 
In general, our rules for which method of polymorphism to use are as follows:

1. Use Duck Typing when you need rapid prototyping or are interacting with simple, informal behaviors. 
2. Use ABCs when you want to enforce a rigid "Is-A" hierarchy and provide shared logic/state across many subclasses. 
3. Use Protocols when you want to define "Can-Do" capabilities (interfaces) that shouldn't require inheritance or interfere with third-party library objects. 
4. Always respect LSP to ensure your polymorphic substitutions don't break the system. 
 
Of course, there will always be caveat examples.  However, 99.9% of the time, these rules apply.  By mastering these three types of polymorphism, you can write Python code that is both highly flexible and robust enough for production systems! 
