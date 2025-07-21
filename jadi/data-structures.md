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

## Strings

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

### String methods
Here’s a **brief list of very important Python string methods** that you'll use often:

| Method              | Description                                  | Example                            |
| ------------------- | -------------------------------------------- | ---------------------------------- |
| `str.lower()`       | Converts to lowercase                        | `'Ali'.lower() → 'ali'`            |
| `str.upper()`       | Converts to uppercase                        | `'Ali'.upper() → 'ALI'`            |
| `str.strip()`       | Removes leading/trailing whitespace          | `'  hi  '.strip() → 'hi'`          |
| `str.replace(a, b)` | Replaces all `a` with `b`                    | `'a.b'.replace('.', '-') → 'a-b'`  |
| `str.split(sep)`    | Splits string into a list                    | `'a,b'.split(',') → ['a', 'b']`    |
| `str.join(list)`    | Joins list into string with separator        | `'-'.join(['a','b']) → 'a-b'`      |
| `str.startswith(x)` | Checks if string starts with `x`             | `'abc'.startswith('a') → True`     |
| `str.endswith(x)`   | Checks if string ends with `x`               | `'abc'.endswith('c') → True`       |
| `str.find(x)`       | Finds index of `x`, or `-1` if not found     | `'abc'.find('b') → 1`              |
| `str.isdigit()`     | Checks if string contains only digits        | `'123'.isdigit() → True`           |
| `str.isalpha()`     | Checks if string contains only letters       | `'abc'.isalpha() → True`           |
| `str.format()`      | Formats string with placeholders             | `'Hi {}'.format('Ali') → 'Hi Ali'` |
| `f"...{var}..."`    | **f-strings** – inline variable substitution | `f'Hi {name}'`                     |

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
here `{age:3.1f}` means:
- take 3 places for the whole number, with 1 decimal, and as float 

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
