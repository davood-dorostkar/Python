# Object-Oriented Programming (OOP)

Object-Oriented Programming helps organize code by bundling **data (attributes)** and **behavior (methods)** into **classes** and **objects**.


## 📌 Key Concepts

* In Python, **everything is an object** — even integers, strings, and functions.
* A **class** is a blueprint for creating objects.
* Objects have:

  * **Attributes** (data/state)
  * **Methods** (functions/behavior)


## 🧩 Defining a Class and Creating Objects

```python
class Person:
    def __init__(self, name):
        self.name = name  # instance attribute

    def greet(self):
        print(f"Hello, I'm {self.name}!")

p = Person("Alice")  # instantiation
p.greet()            # method call using dot operator
```

* `__init__()` is the **constructor** that runs when the object is created.
* `self` refers to the **current instance** of the class.


## 🧠 Instance Attributes vs Class Attributes

* **Instance attributes** are unique to each object.
* **Class attributes** are shared across all instances of the class.

```python
class MyClass:
    shared = 1  # Class attribute

    def __init__(self):
        self.unique = 2  # Instance attribute

obj1 = MyClass()
obj2 = MyClass()

print(obj1.shared)  # 1
print(obj2.shared)  # 1

obj1.shared = 100   # Creates an instance attribute on obj1

print(obj1.shared)  # 100 (instance shadows class attribute)
print(obj2.shared)  # 1   (still refers to class attribute)
print(MyClass.shared)  # 1

MyClass.shared = 42
print(obj1.shared)  # 100 (unchanged)
print(obj2.shared)  # 42 (updated class attribute)

del obj1.shared
print(obj1.shared)  # 42 (falls back to class attribute)
```

🧠 **Tip**: Only modify class attributes through the class itself, not through instances.


## 🧬 Inheritance

You can create a new class based on an existing one.
This allows **code reuse** and **extensibility**.

```python
class Animal:
    def __init__(self, size):
        self.size = size

    def move(self):
        print("Animal moves")

class Cat(Animal):
    def __init__(self, size, breed):
        super().__init__(size)  # Preferred
        # is also correct: Animal.__init__(...)
        self.breed = breed

    def move(self):
        print("Cat runs gracefully")

a = Animal(10)
a.move()  # Animal moves

c = Cat(3, "Persian")
c.move()  # Cat runs gracefully
```

✅ Use `super().__init__()` to call the parent constructor.


## 🧱 Abstract Classes

You can define base classes that **should not be instantiated directly**, but are meant to be inherited.
They often contain **abstract methods** that must be implemented by subclasses.

```python
class Human:
    def __init__(self, name):
        self.name = name

    def walk(self):
        raise NotImplementedError("Subclasses must implement this method")
```

Using it without implementation causes an error:

```python
class Runner(Human):
    def drink(self):
        print("Drinks water")

jack = Runner("Jack")
jack.walk()  # ❌ Raises NotImplementedError
```

Correct way:

```python
class Runner(Human):
    def walk(self):
        print("Runs fast")

jack = Runner("Jack")
jack.walk()  # ✅ Runs fast
```

🧠 This pattern ensures every subclass **must implement** the required methods.


## 🪄 Special / Magic / Dunder Methods

**Dunder methods** are special methods surrounded by double underscores (`__name__`).
They let you define how your objects behave with built-in functions and operators.

### 🔹 Common dunder methods:

| Method     | Purpose                         | Example Use             |
| ---------- | ------------------------------- | ----------------------- |
| `__init__` | Constructor                     | `obj = MyClass()`       |
| `__del__`  | Destructor                      | Automatically on delete |
| `__str__`  | String representation           | `print(obj)`            |
| `__repr__` | Official string (for debugging) | `repr(obj)`             |
| `__len__`  | Length of object                | `len(obj)`              |
| `__eq__`   | Equality check (`==`)           | `obj1 == obj2`          |

### 🔹 Example:

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} with {self.pages} pages"

    def __repr__(self):
        return f"Book(title= {self.title}, pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.pages == other.pages
        return False

    def __del__(self):
        print(f"Book {self.title} is being deleted")

# Usage:
book1 = Book("1984", 328)
book2 = Book("1984", 328)
book3 = Book("Brave New World", 288)

print(book1)         # 1984 with 328 pages
print(repr(book1))   # Book(title=1984, pages=328)
print(len(book1))    # 328
print(book1 == book2)  # True
print(book1 == book3)  # False

del book1  # Triggers __del__ method
```