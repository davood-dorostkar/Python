# Data Structures

## Precedence

| Effective Precedence | Operator(s)         | Description                    | Associativity |
| -------------------- | ------------------- | ------------------------------ | ------------- |
| Highest              | `()`                | **Grouping (parentheses)**     | N/A           |
| 1                    | `**`                | Exponentiation                 | Right-to-left |
| 2                    | `+x`, `-x`, `~x`    | Unary plus, minus, bitwise NOT | Right-to-left |
| 3                    | `*`, `/`, `//`, `%` | Multiplication, division, etc. | Left-to-right |
| 4                    | `+`, `-`            | Addition, subtraction          | Left-to-right |

## Operators

- in python 3.0, `/` always returns a float.
- `//` returns the integer result.
- `%` is the mod operator, `10%3 = 1`

## Numbers

- `1_000_000` is equal to `1000000`

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

### 🔹 How to avoid the space?

If you don’t want the space, either:

1. **Use string concatenation**:

   ```python
   print(a + str(b))  # Outputs: ali2
   ```

2. **Change `sep` parameter**:

   ```python
   print(a, b, sep='')  # Outputs: ali2
   ```

## Types
you can check var type with:
```py
type(msg)
```

>in python almost everything is a class. it means that you can use `.` to access the methods that exist in that class. for example:
```py
name = "Davood"
print(name.lower()) # 'davood'
```
because `name` is a `str` class object.

## String

a string is a list of characters:
```py
msg = "Hello world"
print(msg[0]) # prints: 'H'
```

multi-line string:
```py
msg = """Hi I am davood
this is a python test code
here is a special char \" inside a string
"""
```

- string's chars are immutable in python. you cannot change one char in a string:
    ```py
    msg = "Hello world"
    msg[0] = 'S' # Error
    ```
    you must change the whole string:
    ```py
    msg = 'S' + msg[1:]
    ```

- strings can be multiplied:
```py
msg = "davood"
print((msg + ' ') * 3) # davood davood davood 
```

### 🔹 String methods

| Method              | Description                                  | Example                          |
| ------------------- | -------------------------------------------- | -------------------------------- |
| `str.lower()`       | Converts to lowercase                        | `'Ali'.lower() 'ali'`            |
| `str.upper()`       | Converts to uppercase                        | `'Ali'.upper() 'ALI'`            |
| `str.strip()`       | Removes leading/trailing whitespace          | `'  hi  '.strip() 'hi'`          |
| `str.replace(a, b)` | Replaces all `a` with `b`                    | `'a.b'.replace('.', '-') 'a-b'`  |
| `str.split(sep)`    | Splits string into a list                    | `'a,b'.split(',') ['a', 'b']`    |
| `str.join(list)`    | Joins list into string with separator        | `'-'.join(['a','b']) 'a-b'`      |
| `str.startswith(x)` | Checks if string starts with `x`             | `'abc'.startswith('a') True`     |
| `str.endswith(x)`   | Checks if string ends with `x`               | `'abc'.endswith('c') True`       |
| `str.find(x)`       | Finds index of `x`, or `-1` if not found     | `'abc'.find('b') 1`              |
| `str.isdigit()`     | Checks if string contains only digits        | `'123'.isdigit() True`           |
| `str.isalpha()`     | Checks if string contains only letters       | `'abc'.isalpha() True`           |
| `str.format()`      | Formats string with placeholders             | `'Hi {}'.format('Ali') 'Hi Ali'` |
| `f"...{var}..."`    | **f-strings** – inline variable substitution | `f'Hi {name}'`                   |

- you can use indexes in `str.format`. it gives you more control:
```py
template = "Hello {0}, you have {1} new messages. {0}, don't forget to reply."
result = template.format("Ali", 5)
print(result) # Hello Ali, you have 5 new messages. Ali, don't forget to reply.
```
- you can also use var names:
```py
template = "Hello {name}, you are {age:3.1f} years old."
result = template.format(name="Ali", age=25.666)
print(result)
```
>here `{age:3.1f}` means: take 3 places for the whole number, with 1 decimal, and as float 

## Slicing

a slice is part of a list. example: `msg[n:m]`. the `n` is included, the `m` is not included. in math it is `[a,b)`.

```py
msg = "0123456789"
msg[0:4] # '0123'
```

slicing with `step`:
```py
msg = "0123456789"
msg[0:9:2] # '02468'
```

the negative index starts from the end:
```py
msg[-1] # '9'
```

however in slicing, the negetive index starts from one behind the end:
```py
msg[1:-1] # '12345678'
```

if you want up to the end, leave it blank:
```py
msg[1:] # '123456789'
```

reverse the order:
```py
msg[::-1] # '9876543210'
```

## List

- it is an ordered data structure, also called as arrays in other languages.
- everything about `indexing` and `slicing` works for lists as well.
- items of a list can be of different types, unlike in C.
    ```py
    my_list = ['a', 'davood', 1, 3.14, True]
    ```
- an exact-index selection of a list is no longer a list, but a slice of a list is still a list, even if it is one item
    ```py
    print(my_list[1:2]) # ['davood']
    print(my_list[1]) # davood
    ```
- `len()` is a python built-in function that works on any data structure like lists, and is not a list-specific method.


### 🔹 List Methods


| Method             | Description                                     | Example                     |
| ------------------ | ----------------------------------------------- | --------------------------- |
| `append(x)`        | Adds item `x` to the end                        | `lst.append(10)`            |
| `extend(iterable)` | Adds all items from another iterable            | `lst.extend([1, 2])`        |
| `insert(i, x)`     | Inserts `x` at index `i`                        | `lst.insert(1, 99)`         |
| `remove(x)`        | Removes **first** occurrence of `x`             | `lst.remove(3)`             |
| `pop([i])`         | Removes and returns item at index `i` (or last) | `lst.pop()` or `lst.pop(0)` |
| `index(x)`         | Returns index of **first** occurrence of `x`    | `lst.index(4)`              |
| `count(x)`         | Counts how many times `x` appears               | `lst.count(7)`              |
| `sort()`           | Sorts the list in place                         | `lst.sort()`                |
| `reverse()`        | Reverses the list in place                      | `lst.reverse()`             |
| `copy()`           | Returns a shallow copy of the list              | `lst2 = lst.copy()`         |
| `clear()`          | Removes all items from the list                 | `lst.clear()`               |

Absolutely! Here's a **very brief tutorial for `dict` in Python**, covering the essentials you asked for:

---

## Dictionary

### 🔹 Create a dictionary:

```python
person = {"name": "Ali", "age": 30, "hobbies": ["reading", "guitar"]}
```

### 🔹 Accessing values:

```python
print(person["name"])      # 'Ali'
print(person["city"])      # crashes
print(person.get("age"))   # 30
print(person.get("city"))  # None (doesn't crash!)
print(person.get("city", "-1"))  # -1
```

### 🔹 Dictionary views:

```python
person.keys()     # dict_keys(['name', 'age', 'hobbies'])
person.values()   # dict_values(['Ali', 30, ['reading', 'guitar']])
person.items()    # dict_items([('name', 'Ali'), ('age', 30), ...])
```
>All above methods return a `special view object` that behave like dynamic read-only `sets`, so you can iterate on the result. They behave like sets and can be converted to lists easily:

```python
list(person.keys())     # ['name', 'age', 'hobbies']
```


### 🔹 Adding new items 

**method 1:**
```python
person = {"name": "Ali", "age": 30}
person["city"] = "Tehran"
```

**method 2:**
```python
person.update({"email": "ali@example.com", "job": "Engineer"})
```
After `update()`:

```python
{
    'name': 'Ali',
    'age': 30,
    'city': 'Tehran',
    'email': 'ali@example.com',
    'job': 'Engineer'
}
```

Both approaches work — `[]` is more direct, `update()` is useful for adding many items at once.

### 🔹 Nested dictionary:

```python
data = {
    "user1": {"name": "Ali", "age": 30},
    "user2": {"name": "Sara", "age": 25}
}
print(data["user1"]["name"])  # 'Ali'
```

### 🔹 List inside dictionary:

```python
profile = {
    "name": "Ali",
    "skills": ["Python", "C++", "ROS"]
}
print(profile["skills"][1])  # 'C++'
```


### 🔹 Dictionary Methods

| Method                 | Description                                | Example                |
| ---------------------- | ------------------------------------------ | ---------------------- |
| `get(k)` / `get(k, d)` | Returns value or `d` if `k` not found      | `d.get("x", 0)`        |
| `keys()`               | Returns all keys                           | `d.keys()`             |
| `values()`             | Returns all values                         | `d.values()`           |
| `items()`              | Returns key-value pairs                    | `d.items()`            |
| `update(d2)`           | add another dict to the current one        | `d.update(d2)`         |
| `pop(k)` / `pop(k, d)` | Removes key and returns value (or default) | `d.pop("x", 0)`        |
| `popitem()`            | Removes & returns last (key, value) pair   | `d.popitem()`          |
| `clear()`              | Removes all items                          | `d.clear()`            |
| `copy()`               | Shallow copy of dict                       | `new = d.copy()`       |
| `setdefault(k, d)`     | Returns value; sets key to `d` if missing  | `d.setdefault("x", 0)` |

## Tuple

tuples are just like the lists, with all of their functionalities, except two things:
- syntax is `(...)` instead of `[...]`.
- tuple is `immutable`, so you cannot change any items after initialized.

### 🔹 why use tuples?
tuples are better in performance and memory, so is some cases they are preferred:
- if an object will not be changed
- to return from a function and get the values:
```py
result = (1, 2)
val1, val2 = result
```

## Set

it is an unordered list of items, that each item is unique.

### 🔹 Creating a set:

```python
s = set()               # Empty set
nums = set([1, 2, 3])   # Set with values
nums = {1, 2, 3}        # Set with values
```

> ⚠️ `{}` by itself creates an empty **dict**, not a set.


### 🔹 Adding items:

```python
nums.add(4)
print(nums)  # {1, 2, 3, 4}
```

### 🔹 Set union:

```python
a = {1, 2}
b = {2, 3}
print(a.union(b))      # {1, 2, 3}
```

You can also use the `|` operator:

```python
print(a | b)           # {1, 2, 3}
```

### 🔹 Set intersection:

```python
print(a.intersection(b))  #  2}
```

Or using the `&` operator:

```python
print(a & b)              # {2}
```

### 🔹 Set Methods

| Method / Operator              | Description                          | Example                      |     |     |
| ------------------------------ | ------------------------------------ | ---------------------------- | --- | --- |
| `add(x)`                       | Adds item `x`                        | `s.add(10)`                  |     |     |
| `remove(x)`                    | Removes item (KeyError if not found) | `s.remove(2)`                |     |     |
| `discard(x)`                   | Removes item if present (no error)   | `s.discard(5)`               |     |     |
| `clear()`                      | Empties the set                      | `s.clear()`                  |     |     |
| `union(other)` / `\|`          | Combines sets                        | `s1.union(s2)` or `s1 \| s2` |     |
| `intersection(other)` / `&`    | Common elements                      | `s1 & s2`                    |     |     |
| `difference(other)` / `-`      | Items in first not in second         | `s1 - s2`                    |     |     |
| `symmetric_difference()` / `^` | Items in one but not both            | `s1 ^ s2`                    |     |     |
| `copy()`                       | Shallow copy                         | `s2 = s1.copy()`             |     |     |
| `len(s)`                       | Number of elements                   | `len(s)`                     |     |     |
| `in`, `not in`                 | Membership test                      | `3 in s`                     |     |     |


### 🔹 Set Limitations
sets in Python can only contain *hashable* (immutable) items.


A `set` can contain any object that is:

1. **Hashable** (has a fixed `__hash__()` value during its lifetime)
2. **Immutable** (its contents don’t change — directly or indirectly)

#### ✅ Allowed types (common):

* `int`, `float`
* `str`, `bool`
* `tuple` (if it contains only hashable types)
* `frozenset`
* **Custom class instances** (like your `Person`) — as long as their `__hash__()` and `__eq__()` behave properly

#### ❌ Disallowed types (unhashable):

* `list`
* `dict`
* `set` (yes, even another regular set)
* `tuple` that contains a `list` or other unhashable type


## Booleans

```python
True   # Equivalent to 1
False  # Equivalent to 0
```

### 🔹 `bool()` Conversion

| Value             | `bool(value)` | Notes                      |
| ----------------- | ------------- | -------------------------- |
| `0`, `0.0`        | `False`       | Numbers: 0 is False        |
| `''`, `[]`, `{}`  | `False`       | Empty containers are False |
| `None`            | `False`       | `None` is always False     |
| `'a'`, `[1]`, `1` | `True`        | Non-empty/non-zero is True |

```python
bool(0)         # False
bool("hello")   # True
```

### 🔹 Comparison Operators

| Operator | Meaning               | Example  | Result  |
| -------- | --------------------- | -------- | ------- |
| `==`     | Equal to              | `3 == 3` | `True`  |
| `!=`     | Not equal to          | `4 != 3` | `True`  |
| `<`      | Less than             | `2 < 3`  | `True`  |
| `>`      | Greater than          | `5 > 2`  | `True`  |
| `<=`     | Less than or equal    | `3 <= 3` | `True`  |
| `>=`     | Greater than or equal | `3 >= 4` | `False` |

### 🔹 Logical Operators

| Operator | Description                | Example          | Result  |
| -------- | -------------------------- | ---------------- | ------- |
| `and`    | True if **both** are true  | `True and False` | `False` |
| `or`     | True if **either** is true | `True or False`  | `True`  |
| `not`    | Negates the value          | `not True`       | `False` |

### 🔹 Short-circuit behavior:

```python
False and print("Nope")  # Doesn't print
True or print("Skipped") # Doesn't print
```

### 🔹 `in` and `not in` Operators

| Operator | Description       | Example            | Result |
| -------- | ----------------- | ------------------ | ------ |
| `in`     | Checks membership | `'a' in 'cat'`     | `True` |
| `not in` | Checks absence    | `5 not in [1,2,3]` | `True` |


### 🔹 Booleans as Integers

```python
int(True)    # 1
int(False)   # 0
True + True  # 2
```

Booleans are actually a subclass of `int`:

```python
isinstance(True, int)  # True
```

Absolutely! Here's a **clear and compact guide** to Python's **file I/O (`file` type)** covering everything you asked: opening, reading, modes, `with` block usage, and method behaviors.

---

## File I/O 

### 🔹 Opening a file

```python
f = open("data.txt")  # Open for reading
```

> Returns a **file object**.

### 🔹 File Open Modes

| Mode   | Meaning                | Notes                                     |
| ------ | ---------------------- | ----------------------------------------- |
| `'r'`  | Read-only              | File must exist                           |
| `'w'`  | Write (truncate)       | Creates or overwrites file                |
| `'x'`  | Write (fail if exists) | Raises error if file exists               |
| `'a'`  | Append                 | Adds to end; creates file if missing      |
| `'r+'` | Read and write         | File must exist                           |
| `'b'`  | Binary mode            | Combine with others like `'rb'` or `'wb'` |
| `'t'`  | Text mode (default)    | Combine like `'rt'`, `'wt'`               |


### ⚠️ `close()` is important

* Until `f.close()` is called (or the file object is garbage collected), **OS-level buffers may not write all data to disk**.
* This means changes may not be visible to other processes or programs.
* Also the file cannot be changed or deleted from somewhere else, because the file is being used.

### 🔹 Safe file handling with `with`

```python
with open("data.txt", "r") as f:
    content = f.read()
```

* Automatically **closes** the file when block exits
* Prevents errors or data loss from forgetting `close()`

### 🔹 File Pointer (Cursor)

```python
f.read()   # Reads from the current position
f.seek(0)  # Moves the cursor to the beginning
```

- Use `seek(0)` to reset and re-read from the start.
- When you run `f.read()`, the cursor will reach the end of file, so if you re-read it, it will return nothing.


### 🔹 File Methods

| Method             | Description                               |
| ------------------ | ----------------------------------------- |
| `read()`           | Reads entire content as a single string   |
| `readline()`       | Reads the next line                       |
| `readlines()`      | All lines as a list                       |
| `write(str)`       | Writes string to file                     |
| `writelines(list)` | Writes list of strings                    |
| `seek(offset)`     | Moves file pointer to given byte position |
| `tell()`           | Returns current file pointer position     |
| `close()`          | Closes file                               |
| `flush()`          | Forces write to disk (buffer flush)       |
