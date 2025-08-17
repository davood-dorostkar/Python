# Methods & Functions

## 📌 Methods

In Python, **everything is an object** (i.e., an instance of a class).
**Methods** are functions that belong to objects and are called using dot notation:

```python
mylist = [1, 2, 3]
mylist.append(4)  # append() is a method of list
```

🔍 To get help about a method, use:

```python
help(mylist.pop)
```


## 📌 Functions

A **function** is a reusable block of code that helps avoid repetition.
Writing modular code with functions makes your program **easier to understand, test, and maintain**.

```python
def avg(a, b):
    return (a + b) / 2
```

✅ **Best Practice**:
Functions should ideally **return values**, not print them, so they remain reusable in different contexts.

🧠 You can also **define a function inside another function** (called a **nested function**):

```python
def outer():
    def inner():
        return "Hi from inner"
    return inner()
```


## Functions with Default Arguments

You can specify default values for parameters:

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())         # Hello, Guest!
print(greet("Alice"))  # Hello, Alice!
```


## Positional & Keyword Arguments

You can pass arguments by position or by name:

```python
def say_hello(name, age):
    print(f"{name} is {age} years old.")

say_hello("Bob", 25)              # Positional
say_hello(age=30, name="Charlie") # Keyword (non-positional)
```


Here’s the improved **`*args` and `**kwargs`** section with clearer and deeper explanations, examples, and analogies, in Markdown format:

---

## `*args` and `**kwargs`

Sometimes, you don't know in advance how many arguments a function will receive. Python gives you two powerful tools to handle such cases:

### ✅ `*args` — Variable Positional Arguments

* `*args` allows you to pass **any number of positional (unnamed) arguments** to a function.
* Inside the function, `args` will be a **tuple** containing all the extra values.

```python
def greet_all(*args):
    for name in args:
        print(f"Hello, {name}!")

greet_all("Ali", "Sara", "John")
# Hello, Ali!
# Hello, Sara!
# Hello, John!
```


### ✅ `**kwargs` — Variable Keyword Arguments

* `**kwargs` allows you to pass **any number of named arguments** (i.e., key=value pairs).
* Inside the function, `kwargs` becomes a **dictionary**.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Berlin")
# name: Alice
# age: 30
# city: Berlin
```

### 🔁 You can combine `*args` and `**kwargs` in the same function:

Just make sure `*args` comes **before** `**kwargs`:

```python
def describe(title, *args, **kwargs):
    print(f"Title: {title}")
    print("Positional args:", args)
    print("Keyword args:", kwargs)

describe("Report", 2024, "Q1", author="Alice", pages=5)
# Title: Report
# Positional args: (2024, 'Q1')
# Keyword args: {'author': 'Alice', 'pages': 5}
```

## `lambda` Functions

`lambda` is used to create **small anonymous functions**:

```python
data = [1, 4, 2, 6]
data_sq = map(lambda x: x**2, data)
print(list(data_sq))  # [1, 16, 4, 36]
```

Another example:

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12
```

## LEGB Rule in Python

Python uses the **LEGB rule** to resolve variable names:

* **L**ocal — inside the current function.
* **E**nclosing — inside outer functions.
* **G**lobal — at the module level.
* **B**uilt-in — Python’s built-in names.

Example:

```python
def test():
    name = 'david'
    print(f'in function: {name}')

name = 'alex'
print(f'name in main: {name}')  # alex
test()                          # david
print(f'name in main: {name}')  # alex
```

Even if you don’t redefine `name` inside the function:

```python
def test():
    print(f'in function: {name}')
```

It will use the **global** `name` if it's not found locally.


## `global` Keyword

If you need to **modify a global variable** inside a function, use `global` — but this is **not recommended** in most cases.

```python
count = 0

def increment():
    global count
    count += 1
```

Why not recommended? Because it makes the code **harder to debug and understand**.

## `map()` Function

Apply a function to all items in an iterable:

```python
def square(x):
    return x ** 2

data = [1, 4, 2, 6]
result = map(square, data)
print(list(result))  # [1, 16, 4, 36]
```

Note: `map()` returns a **lazy object**. Convert it to a list to see results immediately.

## `filter()` Function

Used to filter elements based on a condition:

```python
def is_float(x):
    return x != int(x)

data = [1, 4, 2.1, 6]
filtered = filter(is_float, data)
print(list(filtered))  # [2.1]
```

## `zip()`

Pairs items from multiple iterables together.

```python
names = ["Ali", "Sara"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
```
every item in the zip is a tuple:
```
('Ali', 90)
('Sara', 85)
```

## `max()`, `min()`

Return the largest/smallest item in an iterable.

```python
max([3, 1, 4])  # → 4
min("hello")   # → 'e' (alphabetically smallest)
```


## `randint()`

Generates a **random integer** in a given range.

```python
from random import randint
x = randint(1, 6)  # Random int between 1 and 6 (inclusive on both sides)
```

## print()

Internally, `print()` uses the `sep` parameter to separate multiple items:

```python
print(a, b, sep=' ')
```

By default, `sep=' '` (a single space), so:

```python
print('ali', 2)
```

prints:

```
ali 2
```

### How to avoid the space?

If you don’t want the space, either:

1. **Use string concatenation**:

   ```python
   print(a + str(b))  # Outputs: ali2
   ```

2. **Change `sep` parameter**:

   ```python
   print(a, b, sep='')  # Outputs: ali2
   ```

## Function Object
a function is an object that we can use directly instead of calling it.
```py
def say_hello():
    print('hello world')


print(say_hello) # printing the object info: <function say_hello at 0x70aed8d96340>
```
- this way we can pass functions as arguments:
```py
def add(a, b):
    return a + b

def calc(a, b, func):
    return func(a, b)

result = calc(1, 4, add)
print(result)
```
- you also can assign functions to another object (e.g. *functions are first-class citizens*):
```py
def add(a, b):
    return a + b

addition = add

print(add)          # <function add at 0x7bf5731da340>
print(addition)     # <function add at 0x7bf5731da340>
```
if you do so, the second object will point to the same thing, and if the first one is deleted (`del add`), the second one will still exist (like `shared pointers`).