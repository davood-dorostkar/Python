
# 🛠️ Error Handling - Code Quality - Testing

Writing robust Python code means more than just "making it work." You need to **handle errors**, **follow good coding practices**, and **write tests** to ensure your programs work reliably over time.

## ⚠️ 1. Error Handling with `try`/`except`

Python provides a clean way to catch and handle errors using:

```python
try:
    # code that might fail
except:
    # code to run if there's an error
```

This prevents your program from **crashing** unexpectedly when something goes wrong.


### 🔹Good vs Bad Practices

#### ❌ Bad Practice:

* Wrapping huge blocks of code in one big `try`.
* Using `try` just to avoid writing proper checks without understanding it.


#### ✅ Good Practice:

* Keep `try` blocks **short and specific**.
* Only use `try` for operations that are **out of your control**, like:

  * File I/O
  * Network connections
  * User input
* Handle **known exceptions** to give meaningful messages.


### 🔹Basic Exception Handling

```python
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(f"Error: {e}")
        return None

print(divide(3, 4))  # Works
print(divide(3, 0))  # ZeroDivisionError
```

### 🔹Handling Specific Exceptions

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Inputs must be numbers")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

print(divide(3, 0))
print(divide("a", False))
```

You can find all built-in exception types in the [Python Exception Docs](https://docs.python.org/3/library/exceptions.html).


### 🔹Complete Exception Handling Structure

```python
try:
    # Try to do something
except:
    # Handle errors
else:
    # Run this if no exception happened
finally:
    # Always run this (cleanups, closing files, etc.)
```

#### Example:

```python
try:
    x = 1 / 1
except ZeroDivisionError:
    print("Divide by zero error")
else:
    print("Division succeeded")
finally:
    print("Cleanup done")
```

**Benefits**:

* `else`: keeps success logic clean, so you can take other logic out of critical area.
* `finally`: ensures cleanup no matter what happens (e.g., closing a file)


## 🧼 2. Formatters and Linters

### 🔹Formatter

A **formatter** automatically adjusts your code's formatting (indentation, spacing, etc.) without changing behavior.

* Example tool: [`black`](https://black.readthedocs.io)

```bash
pip install black
black myscript.py
```


### 🔹Linter

A **linter** goes beyond formatting — it detects **code smells**, **bad practices**, and even **logic issues**.

* Example tool: [`pylint`](https://pylint.pycqa.org/)

```bash
pip install pylint
pylint myscript.py
```

To generate a summary report:

```bash
pylint --report=y myscript.py
```

### 🔹PEP 8

PEP stands for **Python Enhancement Proposal**.
[PEP 8](https://peps.python.org/pep-0008/) is the style guide for writing clean and readable Python code. Linters like `pylint` help you follow this guide.


>Most modern IDEs support both with plugins or built-in support.


## ✅ 3. Writing Unit Tests with `unittest`

As programs grow, changes can introduce **bugs**. To ensure everything still works, you should write **automated tests**.

Python’s built-in `unittest` module helps you do that.


### 🔹Basic Structure of a Unit Test

```python
import unittest

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_divide(self):
        self.assertEqual(6 / 2, 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == '__main__':
    unittest.main()
```


### 🔹More Test Methods

| Method                | Description                        |
| --------------------- | ---------------------------------- |
| `assertEqual(a, b)`   | Check if `a == b`                  |
| `assertTrue(x)`       | Check if `x` is `True`             |
| `assertFalse(x)`      | Check if `x` is `False`            |
| `assertRaises(Error)` | Check if a certain error is raised |


### 🔹Library vs Framework

| Term          | Description                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------- |
| **Library**   | A collection of tools you **use** from your code (e.g., `math`, `requests`)                |
| **Framework** | A structure that **uses your code**, often enforces structure (e.g., `unittest`, `Django`) |
