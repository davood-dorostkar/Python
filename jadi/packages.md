# Packages

- there are a lot of libraries for almost everything in python
- to find a package for your work, you can:
  - search on google
  - search on PyPi (python package index)
- install a package
  you need to install the external (3rd party) packages before use
  
  ```pip install emoji```
  - installing on different versions of python: `pip3.12 install emoji`
  - install on debian: `apt install python3-emoji`
- ways to use a package:
  - ```import numpy```

  what does it mean
  - ```from numpy import arange```

  what does it mean

- some cool packages:
```python
requests # handle HTTP network flows
tqdm # make cool visual progress bars
# other libraries
```

- creating a module
create a `.py` file, it can contain anything: functions, classes, or variables.

then import it or import a part of it.

you can use it alongside your main file. but if you want to put it inside a directory and want python to understand the directory as a `package`, you must put a `__init__.py` file in the directory as well.

  - if using a simple file alongside your main:

    if want to import the whole file:
    ```py
    import myfile
    m = myfile.myclass()
    ```
    if want to import a part of file:
    ```py
    from myfile import myclass
    m = myclass()
    ```
  - if using a directory:

    if want to import the whole file:
    ```py
    from mydirectory import myfile
    m = myfile.myclass()
    ```
    if want to import a part of file:
    ```py
    from mydirectory.myfile import myclass
    m = myclass()
    ```

**difference of package and module put here**


- __name__
this is a `variable` that always exist in python codes by default. if the file is executed directly this variable is set to the string `"__main__"`, but if it is imported and used in another file, it is set to the package-file structure like `"mypackage.myfile"`.
```py
class myclass():
    def __init__(self):
        print(f"__name__ is set to {__name__}")

if __name__ == "__main__":
    print("this file must be used as a package!")
```
```py
from pypackage import myfile
m = myfile.myclass()

if __name__ == "__main__":
    print("this is the main file!")
```
output:
```
__name__ is set to pypackage.myfile
this is the main file!
```
if you run the package file directly:
```
this file must be used as a package!
```
there are two good practices in this regard:
  - avoid running packages directly (like above)
  - using packages as executables in command line. this way, you can put a section (main) that is executed if the program is run directly. many python packages can be used as a library or as a command this way. for example `tqdm` is a python package, but you can use it as a command and pipe output of another command to it
  **example**

- to install your package
create a structure like:
```
your_project/
├── mylibrary/
│   ├── __init__.py
│   └── library.py
├── main.py
└── setup.py 
```
then in the setup.py:
```py
from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # list dependencies here if any
    author='Your Name',
    description='A simple library management package',
    python_requires='>=3.6',
)
```
then in the project root:
```
pip install . --break-system-packages
```
or for making it editable (recommended for development):
```
pip install -e . --break-system-packages
```