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


## Itertools

The `itertools` module builds **fast, memory-efficient iterators**.

```python
import itertools as it

# cycle → infinite loop through elements
target_ip = it.cycle([
    '10:e7:c6:22:de:81', 
    '52:54:00:6c:78:a4', 
    '12:cd:96:8e:ec:f1'])

for _ in range(5):
    print(next(target_ip))
```

Output cycles through the list repeatedly.


### Other itertools tools

```python
nums = [1, 2, 3, 4]

# Combinations (no repeats)
list(it.combinations(nums, 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# Combinations with replacement
list(it.combinations_with_replacement(nums, 2))
# [(1, 1), (1, 2), ..., (4, 4)]

# Permutations (order matters)
list(it.permutations(nums, 2))
# [(1, 2), (1, 3), ..., (4, 3)]

# Counting
counter = it.count(3, 10)  # start=3, step=10
next(counter)  # 3
next(counter)  # 13

# Accumulate (running totals)
list(it.accumulate(nums))  # [1, 3, 6, 10]

# Cartesian product
l1 = [1, 2]
l2 = ['a', 'b']
list(it.product(l1, l2))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```
