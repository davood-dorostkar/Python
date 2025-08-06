# 📚 Python Standard Library

Python's standard library is full of powerful modules that save time and simplify development.

🔗 Official docs: [Python Standard Library](https://docs.python.org/3/library/index.html)


## 📦 `collections` — Specialized Containers

📄 Docs: [collections](https://docs.python.org/3/library/collections.html)

### 🔹`defaultdict`: Automatically Handles Missing Keys

```python
from collections import defaultdict

# Default type is int (starts at 0)
d = defaultdict(int)
d['apple'] += 1
print(d)  # {'apple': 1}

# You can set any default: list, str, lambda, etc.
d2 = defaultdict(list)
d2['fruits'].append('banana')
print(d2)  # {'fruits': ['banana']}

# Using a custom default:
d3 = defaultdict(lambda: 'not found')
print(d3['missing'])  # 'not found'
```


## ⌚ `datetime` — Dates, Times, and Formatting

📄 Docs: [datetime](https://docs.python.org/3/library/datetime.html)

```python
from datetime import datetime, timedelta, date, time

now = datetime.now()
print(now)              # 2025-08-05 15:30:12.123456
print(now.date())       # 2025-08-05
print(now.time())       # 15:30:12.123456
print(now.year)         # 2025
print(now.month)        # 8
print(now.day)          # 5
print(now.hour)         # 15
print(now.minute)       # 30

# or use more specific modules
print(date.today())     # 2025-08-05 (instead of using the more complete datetime structure)

# Create a specific date or time
d = date(2024, 12, 31)
t = time(10, 30)
print(d, t)

# Or (if you don't specify some values, it will be defaulted to zero)
print(datetime(2025, 3, 12, 4, 25, 50, 100))    # 2025-03-12 04:25:50.000100    
print(datetime(2025, 3, 12, 4, 25, 50))         # 2025-03-12 04:25:50
print(datetime(2025, 3, 12, 4, 25))             # 2025-03-12 04:25:00
print(datetime(2025, 3, 12, 4))                 # 2025-03-12 04:00:00
print(datetime(2025, 3, 12))                    # 2025-03-12 00:00:00
print(datetime(2025, 3))                        # invalid - day is required

# Date formatting
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print(formatted)

# Parse string into datetime
parsed = datetime.strptime("2025-08-05 15:30", "%Y-%m-%d %H:%M")
print(parsed)

# Timedelta for date math
tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow)
```


## 🎲 `random` — Generating Randomness

📄 Docs: [random](https://docs.python.org/3/library/random.html)

```python
import random

# Seed controls randomness (for reproducibility)
random.seed(42)
print(random.randint(1, 6))  # always same output with same seed
print(random.random())       # random float [0,1)

# Pick single value
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))

# Pick unique sample (no repetition)
sample = random.sample(range(1, 50), 6)
print("Lottery numbers:", sample)

# Shuffle a list in place
items = [1, 2, 3, 4]
random.shuffle(items)
print(items)
```

### 🔹 How `seed()` Works

Using `random.seed(x)` sets the internal state of the RNG. Same seed → same results.

Useful for:

* Testing
* Reproducible results in research or demos


## 🔍 `re` — Regular Expressions

📄 Docs: [re](https://docs.python.org/3/library/re.html)

Use regex for matching patterns in strings.

### 🔹 Common Syntax

| Pattern | Meaning        | Pattern | Meaning                    |
| ------- | -------------- | ------- | -------------------------- |
| `\d`    | Digit          | `{3}`   | Exactly 3 times            |
| `\w`    | Word character | `{2,4}` | Between 2 and 4 times      |
| `\s`    | Whitespace     | `^`     | Start of string            |
| `.`     | Any character  | `$`     | End of string              |
| `+`     | One or more    | \+`     | treat string literally (+) |
| `*`     | Zero or more   | `()`    | Grouping                   |
| `?`     | Optional       | `[]`    | Character set              |



### 🔹 Common Functions with Examples

```python
import re

text = "My number is 123-456-7890 and email is test@mail.com"

# re.search
m = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(m.group())  # '123-456-7890'

# re.match (only matches beginning)
m = re.match(r'\w+', text)
print(m.group())  # 'My'

# re.fullmatch
print(re.fullmatch(r'\d+', '123'))  # match object

# re.findall
emails = re.findall(r'\w+@\w+\.\w+', text)
print(emails)  # ['test@mail.com']

# re.finditer
for m in re.finditer(r'\d+', text):
    print(m.group(), m.span())

# re.sub
new = re.sub(r'\d', 'X', text)
print(new)
```


### 🔹 Grouping and Arguments

```python
text = "Name: John, Age: 30"

# Group name and age
m = re.search(r'Name: (\w+), Age: (\d+)', text)
print(m.group(1))  # John
print(m.group(2))  # 30

# Named groups
m = re.search(r'Name: (?P<name>\w+), Age: (?P<age>\d+)', text)
print(m.group('name'))  # John
print(m.group('age'))   # 30
```


### 🔹 Character Sets and Pattern Compilation

```python
# Match words with backtick or word characters
pattern = re.compile(r"[\w`]+")
print(pattern.findall("word1 word2 `inline_code`"))  # ['word1', 'word2', '`inline_code`']

# Match only lines starting with digit
text = "1. one\n2. two\nA. three"
lines = re.findall(r'^\d\..*', text, re.M)
print(lines)  # ['1. one', '2. two']
```


## 🔢 `decimal` — Precise Floating Point Math

📄 Docs: [decimal](https://docs.python.org/3/library/decimal.html)

### Problem: Binary Floating Point Isn’t Exact

```python
print(0.1 + 0.2)         # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False
```

This happens due to **binary floating-point representation**.

### 🔹 Using Decimal for Accuracy

```python
from decimal import Decimal, getcontext

# View precision setting
print(getcontext())  # Default: 28 digits

# Incorrect: floats are already imprecise
print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))  # False

# Correct: use string literals
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # True
```


### 🔹Real Example with Math

```python
nums = '1.2 4.5 5.6 8.2'
from decimal import Decimal
my_list = list(map(Decimal, nums.split()))
print(my_list)             # [Decimal('1.2'), Decimal('4.5'), ...]
print(sorted(my_list))     # Accurate sort
print(sum(my_list))        # Precise sum
```
