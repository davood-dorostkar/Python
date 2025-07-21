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