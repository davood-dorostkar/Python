# Conditionals and Loops

## `if` Statement

```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

➡️ Runs **only one matching block** from top to bottom.


## `for` Loops

Used to **iterate** over a range, list, string, or other iterable.

```python
for i in range(3):
    print(i)  # → 0 1 2
```

### 🔹 Loop with `_`

Use `_` when you **don’t care about the loop variable**.

```python
for _ in range(5):
    print("Repeat")  # Just repeats 5 times
```

### 🔹 Loop over iterable

Works with any sequence like string, list, etc.

```python
for char in "Ali":
    print(char)
```

### 🔹 Unpacking in loops

You can unpack tuples or pairs directly:

```python
pairs = [(1, 2), (3, 4)]
for a, b in pairs:
    print(a + b)  # → 3 7
```

## Looping on a Dictionary

Use `.items()` to loop through key–value pairs.

```python
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)
```


## `pass`, `break`, `continue`

Control how loops behave:

| Keyword    | Meaning                       |
| ---------- | ----------------------------- |
| `pass`     | Do nothing (placeholder only) |
| `break`    | Exit the **current loop**     |
| `continue` | Skip rest of this iteration   |

### 🔹 In nested loops:

* `break`/`continue` affect **only the innermost loop**.

```python
for i in range(2):
    for j in range(2):
        if j == 1:
            break  # Breaks inner loop only
```


## `while` Loop

Repeats **as long as condition is True**.

```python
x = 3
while x > 0:
    print(x)
    x -= 1
```


## List Comprehension

A compact way to create lists.

```python
squares = [x * x for x in range(5)]
```

```python
[result for item in iterable]
```


## Ternary Operator

Inline **`if-else` expression** for assignments or returns.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

## Ternary + List Comprehension

### 🔹 Condition on the **result**:

```python
["even" if x % 2 == 0 else "odd" for x in range(5)]
# → ['even', 'odd', 'even', 'odd', 'even']
```

### 🔹 Condition on the **loop itself**:

```python
[x for x in range(5) if x % 2 == 0]
# → [0, 2, 4]
```
>both methods result to the same thing. one difference is that in the first method, you must have an `else` section, while in the second method, you can ommit `else`.

## `range()`

Generates a sequence of numbers.

```python
range(5)        # → 0 to 4
range(1, 4)     # → 1 to 3
range(0, 10, 2) # → 0, 2, 4, 6, 8
```


## `enumerate()`

Gives both **index and value** when looping:

```python
lst = ['a', 'b']
for i, val in enumerate(lst):
    print(i, val)  # → (0, 'a'), (1, 'b')
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
