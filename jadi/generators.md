# Generators

**Generators** are special functions in Python that allow you to **pause and resume** execution, making them perfect for handling **large datasets** or **lazy evaluation** (generating values only when needed).

They help you:

* Save memory
* Write cleaner code for custom iterators
* Handle infinite or large sequences efficiently


## 📦 When to Use Generators

Use generators when:

* You’re dealing with **large amounts of data** (e.g., reading large files, generating large sequences)
* You want to avoid **loading everything into memory**
* You need **lazy evaluation** (compute values on demand)
* You want to **simplify custom iterator** logic


## ✅ General Structure 

```python
def my_generator():
    # setup or initial code (runs first)
    yield value1  # pause here and return value1
    # code resumes here after next() is called again
    yield value2
    # code resumes here after another next()
    yield value3
    # ... and so on
```

When the function **hits `yield`**, it:

* **Returns the value**
* **Pauses** the function
* **Resumes** from the same spot next time it's called with `next()`


## 🔁 What is `yield`?

In a normal function, you use `return` to return a value and **exit** the function.

In a **generator**, you use `yield` to return a value and **pause** the function. When the generator is resumed, it continues **from where it left off**.


## 🔢 Simple Example: Countdown Generator

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))  # 3
print(next(gen))  # 2
print(next(gen))  # 1
# print(next(gen))  # Raises StopIteration
```

Each `next()` call resumes the function **from where it was paused**, not from the start.

## 🔄 Looping Over Generators

You usually don't need to use `next()` manually. Instead, you use a `for` loop:

```python
for num in countdown(3):
    print(num)
```

Output:

```
3
2
1
```


## 🧠 How Generators Work Behind the Scenes

A generator function returns a **generator object**:

```python
gen = countdown(3)
print(type(gen))  # <class 'generator'>
```

This object supports the **iterator protocol** — meaning you can call `next()` or use it in a loop.


## 🧰 More Practical Examples

### 1. Dice Roll Generator

```python
def dice_rolls():
    rolls = [(3, 5), (6, 2), (4, 4), (1, 6)]
    for roll in rolls:
        yield roll

gen = dice_rolls()
for roll in dice_rolls():
    print(f"Dice A: {roll[0]}, Dice B: {roll[1]}")
```
Output:

```
Dice A: 3, Dice B: 5
Dice A: 6, Dice B: 2
Dice A: 4, Dice B: 4
Dice A: 1, Dice B: 6
```

### 2. Reading a Large File Lazily

```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

for line in read_lines("big_file.txt"):
    print(line)
```


## 🆚 Generator vs List Comprehension

You can create a generator expression similar to list comprehension:

```python
squares = (x * x for x in range(10))  # range is a generator
```

Compare:

```python
my_list = [x * x for x in range(10)]  # builds full list
my_gen = (x * x for x in range(10))   # creates generator

print(next(my_gen))  # 0
```
you can also turn the generator to a list:
```py
list(my_gen)
```