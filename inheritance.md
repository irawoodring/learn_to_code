# Inheritance in Python

Inheritance is one of the fundamental pillars of Object-Oriented Programming (OOP). In Python, it provides a mechanism where a new class (the subclass or child class) can inherit attributes and methods from an existing class (the superclass or parent class). This promotes the DRY (Don't Repeat Yourself) principle, allows for cleaner code organization, and enables developers to model real-world relationships logically within software.

Before now, we have created new classes using a process called **Composition** - i.e. we composed classes by putting together existing types of data into a new type.  Inheritance doesn't replace composition; instead, it is another tool in your coding toolbox. In this chapter we will dive into inheritance, covering everything from basic syntax to advanced concepts like Method Resolution Order (MRO), Abstract Base Classes, and the nuances of Multiple Inheritance.

---

## The Philosophy of Inheritance

Before writing code, it is vital to understand *why* we use inheritance. In software engineering, inheritance represents an "is-a" relationship.

- A `Manager` **is-a** `Employee`.
- A `SavingsAccount` **is-a** `BankAccount`.
- A `Circle` **is-a** `Shape`.

When you inherit, you are saying that the subclass shares the identity and capabilities of the parent class but adds its own specific traits. If a method exists in the parent class, it should be available to all children unless specifically overridden or restricted.  For instance, in the banking example above, every `BankAccount` probably has an account number.  Therefore, we don't need to explicitly define a `SavingsAccount` as having an account number if we inherit from `BankAccount`.  Since a `SavingsAccount` **is-a** `Bank-Account`, it will get one automatically.

## Basic Syntax and Structure of Inheritance in Python

In Python, inheritance is declared by passing the name of the parent class as a parameter into the child class definition.

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.brand} {self.model} engine is now running.")

class Car(Vehicle):		# NOTE! We passed Vehicle in here!
    def __init__(self, brand, model, door_count):
        # Initialize the parent class attributes
        super().__init__(brand, model)
        self.door_count = door_count

    def open_trunk(self):
        print("Trunk is now open.")

# Instance of subclass
my_car = Car("Tesla", "Model 3", 4)
my_car.start_engine()  # Inherited method
my_car.open_trunk()     # Subclass-specific method
```

Notice the `super().__init__(...)` line; this is calling the parent object's constructor.  It is standard practice to call the parent's `__init__` method, and you must remember to do so.  If you omit this, the child class will not have access to the initialization logic of the parent (like setting `self.brand`).  This is because in many languages, the child object stores only the data defined in the child class, and relies upon an instance of the parent class existing to hold the information defined in the parent.  If we don't explicitly create the parent, then that object won't exist, and we won't have access to that data.

Further, notice that we had to pass the appropriate parameters to the parent object (in this case `brand`, and `model`).  In this example, that means that we needed to take those parameters in the child class (in `Car`'s constructor), or we wouldn't have had those to pass to our parent.

See the line `my_car.start_engine()`?  We are able to call the `start_engine()` method on the object called `my_car` *even though we didn't write code for that method in the `Car` class*.  This is the power of inheritance - since our parent object had that method, we get it too!

## 3. Method Overriding and Specialization

**Overriding** a method occurs when a subclass provides a different implementation for a method already defined in the parent class. This is how we handle "Specialized" behavior.

Imagine a `Vehicle` class where `move()` means something different for a boat versus a car.

```python
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing across the water.")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

boat = Boat()
car = Car()

boat.move()  # Output: The boat is sailing across the water.
car.move()   # Output: The car is driving on the road.
```

**Technical Note:** When you call `car.move()`, Python looks at the `Car` class first. Since it finds a definition for `move` there, it executes that and stops looking further up the chain. This is known implicitly by the interpreter as **shadowing**.  Think of it like this - the `Car` `move()` is hiding or *casting its shadow* over the `Vehicle`'s `move()`, causing it not to be seen.

## 4. The `super()` Function: Extension vs. Replacement

A common mistake beginners make is thinking overriding *must* replace parent functionality. Often, we want to *add* to what the parent does. This is where `super()` becomes indispensable.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is performing standard tasks.")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Keep the basic employee setup
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        # Call parent functionality first
        super().work() 
        print(f"{self.name} is writing code in {self.programming_language}.")

dev = Developer("Alice", 100000, "Python")
dev.work()
# Output:
# Alice is performing standard tasks.
# Alice is writing code in Python.
```

By using `super().work()`, we ensure that the base logic remains consistent across all employees while allowing specific roles to add their unique contributions.

## 5. Multiple Inheritance and Method Resolution Order (MRO)

Python allows a class to inherit from multiple parents. This is powerful but can become complex if not understood correctly.  Because of the problems that can be caused by multiple inheritance some languages (like Java) don't allow it.

```python
class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()   # Flyer logic
d.swim()  # Swimmer logic
```

### How Python Decides: The MRO
When you have a complex hierarchy where multiple parents might share method names, Python uses the **Method Resolution Order (MRO)**. It follows a "Depth-First Search" style but ensures that no class is visited twice in the same path.

You can view this order by calling `.mro()` on any class:
```python
print(Duck.mro())
# Output: [Duck, Flyer, Swimmer, object]
```
The search starts at `Duck`, then looks at `Flyer`, then `Swimmer`, and finally falls back to the base `object` class.

## 6. Abstract Base Classes (ABCs)

Sometimes you want to define a blueprint for a class but you don't want anyone to be able to instantiate that parent directly. You want to *force* subclasses to implement certain methods. This is what **Abstract Base Classes** are for.

You use the `abc` module for this:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# This would throw an error:
# s = Shape()  # TypeError: Can't instantiate abstract class Shape

sq = Square(5)
print(f"Area: {sq.area()}")
```

This might initially seem sort of silly.  After all, we still had to write an `area()` and `permieter()` method in `Square`, just like we had in `Shape`.  So, why use ABCs? They act as a contract. If a developer creates a `Circle` class but forgets to implement the `area` method, Python will raise an error immediately upon instantiation rather than failing later at runtime when the code tries to call a missing method.  Try it!  Modify the code above so that `Square` only has a constructor.  Then, try to create a new `Square`.

## Inheritance vs. Composition (The "Is-A" vs. "Has-A" rule)

As we said at the start of this chapter, inheritance and composition are both just tools in your coding toolbox.  One of the most important architectural decisions in software design is choosing between inheritance and composition.

### When to use Inheritance:
Use inheritance when there is a strict **is-a** relationship and you want to share state and behavior. 
*   `Manager` is an `Employee`.
*   The manager *must* be able to do everything an employee can.

### When to use Composition:
Use composition when there is a **has-a** or **can-do** relationship. Instead of inheriting from a class, you give the object an instance of that class as an attribute.
*   A `Car` has an `Engine`. (Don't inherit from `Engine`).
*   A `Robot` can `Fly`. (Instead of making `FlyingRobot(FlyingMachine)`, give the Robot a `FlightModule`).

**Example of Composition:**
```python
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine_type):
        # The car HAS AN engine, it IS NOT an engine.
        self.engine = engine_type 

    def start_car(self):
        self.engine.start()

gas_engine = Engine()
my_car = Car(gas_engine)
my_car.start_car()
```
Composition is often more flexible because it allows you to swap components at runtime (e.g., changing a `GasEngine` for an `ElectricEngine`) without changing the hierarchy of the class.  But, both composition and inheritance have their place, and we must learn to use each effectively.

## Common Pitfalls and Performance Considerations

### The "Fragile Base Class" Problem
When you have a deep inheritance tree, a small change in a parent class can ripple down and break functionality in dozens of subclasses. This is why **shallow inheritance** (keeping trees 1-2 levels deep) is the industry standard.

### Method Resolution Overhead
While Python’s MRO is efficient, extremely deep nesting or complex multiple inheritance can slightly slow down method lookups. However, for 99% of applications, this is negligible compared to the benefits of code organization.

### Memory Management
Every time you instantiate a subclass, it carries the weight of its parents' attributes. If a parent class has massive data structures that a child doesn't need, those are still carried in memory. This reinforces why **Composition** is preferred for things the child doesn't actually "need."

## Conclusion

Mastering inheritance allows you to build systems that are modular, extensible, and easy for other developers to navigate. By understanding the difference between `super()` calls, MRO, and Abstract Base Classes, you can design architectures that scale from simple scripts to complex enterprise applications.  Just remember the golden rule: **Inherit only when there is a true "is-a" relationship; otherwise, use composition.**
