# 🧩 Decorators

**Decorators** in Python are functions that **modify the behavior of other functions or classes** without changing their source code. They help you write cleaner, DRY (Don't Repeat Yourself) code by abstracting repeated logic.


## 🚀 What Is a Decorator?

At its core, a **decorator is a function that takes another function (or class), wraps it with additional functionality, and returns the enhanced version.**


## 🏠 Login Page Example: The Motivation

### 🟢 Initial Code:

```python
def open_home_page():
    return 'home_page.html'

def open_dashboard_page():
    return 'dashboard.html'

open_home_page()
open_dashboard_page()
```

So far, both pages are accessible without restrictions.


### 🔒 Adding Login Checks (Naive Way)

```python
logged_in = False

def open_home_page():
    if logged_in:
        return 'home_page.html'
    else:
        open_login_page()

def open_dashboard_page():
    if logged_in:
        return 'dashboard.html'
    else:
        open_login_page()
```

**Problem**: The login-check logic is **duplicated** in every function.


### ✅ Using a Wrapper Function

To avoid repeating code:

```python
def check_login(func):
    if logged_in:
        func()
    else: 
        open_login_page()

def open_home_page():
    return 'home_page.html'

def open_dashboard_page():
    return 'dashboard.html'

check_login(open_home_page)
check_login(open_dashboard_page)
```

**Improvement**, but now we must **explicitly pass** functions to `check_login()` each time we call them.


## 🛠️ Writing a Decorator: Basic Structure

With **decorators**, you can **attach logic directly to a function’s definition**, and then call the function as usual.


```python
def decorator(func):
    def wrapper():
        # Do something before or after func()
        return func()
    return wrapper
```

Apply it with `@decorator` above the function **definition**:

```python
@decorator
def my_function():
    ...
```


## 🔐 Login Example Using Decorators

### Simplest Form

```python
logged_in = False

def open_login_page():
    print("login_page.html")

def check_login(func):
    def wrapper():
        if logged_in:
            func()
        else:
            open_login_page()
    return wrapper

@check_login
def open_home_page():
    print("home_page.html")

@check_login
def open_dashboard_page():
    print("dashboard.html")

open_home_page()
open_dashboard_page()

logged_in = True

open_home_page()
open_dashboard_page()
```


## ✅ Best Practices for Decorators

### 1. Always Return from the Decorated Function


```python
def open_login_page():
    print("login_page.html")
    return "login_page.html"
```

Update the wrapper:

```python
def wrapper():
    if logged_in:
        return func()
    else:
        return open_login_page()
```

### 2. Support Function Arguments with `*args`, `**kwargs`

This makes your decorator more flexible and reusable:

```python
def check_login(func):
    def wrapper(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            return open_login_page()
    return wrapper
```

📌 When your function accepts argument, you **must** define arguments in the wrapper. Effectively, the **function name** is passed to the **decorator** (`def timer(f):`) and the **function arguments** are passed to the **wrapper** (`def wrapper(*args, **kwargs):`).

**Example:**
```py
import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        f(*args, **kwargs)
        end = time.perf_counter()
        print(f'time taken: {1000 * (end - start):.3f} milliseconds')
    return wrapper

@timer
def make_list(n):
    my_list = [i for i in range(1, n + 1)]
    print(my_list)

n = int(input('give a number: '))
make_list(n)
```

### 3. Preserve Metadata with `functools.wraps`

Use `@wraps(func)` to keep original function names and docstrings. With `@wraps`, tools like `help(open_home_page)` or `__name__` show the original function name instead of wrapper.

```python
from functools import wraps

def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            return open_login_page()
    return wrapper
```

## 🧰 Python Built-in Decorators

Python provides some **built-in decorators** commonly used in both standard library and real-world projects:

| Decorator              | Use Case                                                                  |
| ---------------------- | ------------------------------------------------------------------------- |
| `@staticmethod`        | Declare a method that doesn’t need access to `self`                       |
| `@classmethod`         | Passes the class (`cls`) instead of the instance (`self`)                 |
| `@property`            | Turns a method into a read-only property                                  |
| `@functools.lru_cache` | Caches function return values to speed up repeated calls                  |
| `@dataclass`           | Automatically adds special methods to a class like `__init__`, `__repr__` |


### Example: `@staticmethod` and `@property`

```python
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @staticmethod
    def say_hello():
        print("Hello!")

u = User("Alice")
print(u.name)     # uses @property
User.say_hello()  # uses @staticmethod
```
