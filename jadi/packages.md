# 📦 Packages

Python has a rich ecosystem of **third-party packages** that make development faster and easier. Whether you're working on web apps, data science, automation, or anything in between, there's likely a Python package that helps.

## 🔍 Finding and Installing Packages

Python has thousands of open-source packages. To find one:

* Search on [Google](https://google.com) for what you need (e.g., "python send email")
* Use the official [PyPI (Python Package Index)](https://pypi.org/) to search and browse packages

### 🔹Installing Packages

Use `pip` (Python's package installer) to install packages.

```bash
pip install emoji
```

If you have multiple Python versions:

```bash
pip3.12 install emoji  # install for Python 3.12
```

If you're on **Debian-based systems** (like Ubuntu), some packages can be installed via `apt`:

```bash
sudo apt install python3-emoji
```


## 🧰 Using a Package

You use `import` to load packages in your Python code.

### 🔹Examples:

```python
import numpy
```

This imports the whole `numpy` library. You can use it like:

```python
numpy.arange(10)
```

```python
from numpy import arange
```

This imports only the `arange` function. You can use it directly:

```python
arange(10)
```


## ✨ Cool Python Packages

Here are a few useful packages to explore:

```python
requests      # makes HTTP requests easy (APIs, web scraping, etc.)
tqdm          # adds progress bars to loops
pandas`       # data analysis and manipulation
matplotlib    # plotting and visualization
flask         # lightweight web development
rich          # rich text formatting for the terminal
```

## 🧱 Creating Your Own Module or Package

### 🔹Modules

A **module** is just a `.py` file that contains Python code: variables, functions, classes, etc.

For example:

`myfile.py`:

```python
class MyClass:
    def say_hello(self):
        print("Hello from MyClass")
```

Using it in `main.py`:

```python
import myfile

obj = myfile.MyClass()
obj.say_hello()
```

Or import just the class:

```python
from myfile import MyClass

obj = MyClass()
```


### 🔹Packages

A **package** is a directory that contains a special file: `__init__.py`. This tells Python it’s a package.

Structure:

```
mydirectory/
├── __init__.py
└── myfile.py
```

Example usage:

```python
from mydirectory import myfile
obj = myfile.MyClass()
```

Or:

```python
from mydirectory.myfile import MyClass
obj = MyClass()
```

❌  **Note: this syntax is invalid:**
```python
from mydirectory import myfile.MyClass
obj = MyClass()
```

### 🔹Module vs Package

| Module                | Package                                       |
| --------------------- | --------------------------------------------- |
| A single `.py` file   | A directory with `__init__.py`                |
| Easier for small code | Useful for organizing large projects          |
| Can be imported       | Can contain multiple modules and sub-packages |

### 🔹Important Update

In Python **3.2 and earlier**, a folder **must** contain an `__init__.py` file (even if it's empty) for Python to recognize it as a package and allow you to import from it. Starting with **Python 3.3**, a feature called **Implicit Namespace Packages** was introduced (via PEP 420). This means that a folder without an `__init__.py` file is **automatically considered a namespace package**.

#### **Use a folder WITH `__init__.py` (Regular Package) when:**
*   **You need initialization code.** The `__init__.py` is executed when the package is imported. You can use it to set up the package environment, consolidate imports, or run other crucial code.
*   **You want to control what gets exported.** A very common use is the `__all__` list, which defines what symbols are imported when someone uses `from your_package import *`.
*   **You need to maintain compatibility with older versions of Python** (anything before 3.3).
*   **You are creating a library for public distribution.** It's the most common, explicit, and expected pattern. It gives you full control over your package's API.

#### Summary

| Feature | **Without `__init__.py`** (Namespace Pkg) | **With `__init__.py`** (Regular Pkg) |
| :--- | :--- | :--- |
| **Python Version** | **>= 3.3** | **All Versions** |
| **Initialization** | Not possible | **Yes** (code runs on import) |
| **API Control** | Limited | **Full control** (using `__all__`) |
| **Common Use** | Simple packages, combining dist. packages | **The standard for most projects** |

**Conclusion:** For most projects, especially those you plan to distribute, **it is still considered best practice to include an `__init__.py` file**. It's the explicit, traditional, and more powerful method. The ability to work without it is a useful modern feature for specific cases, but it doesn't replace the functionality of the traditional package structure.

## 🧠 `__name__` Variable in Python

Python sets a special variable called `__name__` in every script.

* If the script is **run directly**, `__name__ == "__main__"`
* If it's **imported**, `__name__` becomes the module/package name

### 🔹Example:

```python
# myfile.py
class MyClass:
    def __init__(self):
        print(f"__name__ is set to {__name__}")

if __name__ == "__main__":
    print("This file was run directly.")
```

Running `python myfile.py` prints:

```
__name__ is set to __main__
This file was run directly.
```

Importing from another script:

```python
from myfile import MyClass
```

Prints:

```
__name__ is set to myfile
```

### 🔹Best Practices

* Avoid putting logic at the top-level of modules
* Use:

  ```python
  if __name__ == "__main__":
      main()
  ```

  to allow your code to be used **as a script** and **as a library**

#### 🔹Real-world Example

`tqdm` can be used:

* In Python scripts:

  ```python
  from tqdm import tqdm
  for i in tqdm(range(100)):
      ...
  ```
* From the command line:

  ```bash
  some_command | tqdm
  ```


## 📦 Creating and Installing Your Own Package

To share or reuse your code as a package:

### 🔹Project Structure:

```
your_project/
├── mylibrary/
│   ├── __init__.py
│   └── library.py
├── main.py
└── setup.py
```

### 🔹`setup.py` file:

```python
from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    author='Your Name',
    description='A simple Python package',
    python_requires='>=3.6',
)
```

### 🔹Installing the package (from the project root):

Install normally:

```bash
pip install . --break-system-packages
```

Or in **editable** mode (recommended for development):

```bash
pip install -e . --break-system-packages
```

This allows changes in your source files to reflect immediately without reinstalling.
