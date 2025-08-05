# Error Handling

## intro
syntax:
```py
try:
    ###
except:
    ###
```

it is a way to avoid crashing when there is an issue.

## good/bad practices
**bad practice**: 
- create a large try section and put everything in it. you should not just pass the errors by, instead you should actually solve as much errors as you can.
- you should not add try because you are lazy to manage different situations, instead try is for things that you actually have no control over (like network disconnection, etc)

**good practice**: keep the try section short, this way you are actually trying a short part so you can know if that specific part had an error and can handle it accurately. otherwise some part that you did not expect may fail and you confuse.

## exception check
general exception
```py
def divide(a, b):
    try:
        return a/b
    except Exception as e:
        print(f'error: {e}')
        return None
    
divide(3,4)
divide(3,0)
```

you can check multiple known exceptions together, and specify the behavior for speicific sitations:
```py
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('cannot divide by zero')
    except Exception as e:
        print(f'error: {e}')
        return None
    
divide(3,4)
divide(3,0)
divide('a', False)
```
list of all [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

## complete excepion handling flow
```py
try:
    # try this
except:
    # if error happens do this
else: 
    # if error not happens do this
finally:
    # in any case do this
```

**benefits of this structure**

## linter
**formatter** is a program that checks your code for its beauty (indentation, spaces, etc). example: black

**linter** is a program that in addition to format check, can check your logic, bad practices, etc. (long functions, complicated loops, bad namings, case check, etc). example: pylint

### PEP (python enhancement proposal)
a set of guides to make your code better. there are multiple proposals, each describe specific things. one important one is [PEP 8](https://peps.python.org/pep-0008/)

formatters and linters exist for every language. for python:
```sh
pip install pylint
```
then you can use it in terminal:
```sh
pylint prog.py # simple checkign
pylint --report y prog.py # produce a report with tables in terminal
```

you can format it with black:
```sh
pip install black
```
```sh
black prog.py
```

usually IDEs have integrated linter/formatter extensions.   

## Unit test

for large programs if someone changes the code, its hard to ensure if the code is still correct. so you must use automatic tests. in python we use `unittest`. [unittest reference](https://docs.python.org/3/library/unittest.html)

basic structure of `unittest`:
```py
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        with self.assertRaises(TypeError):
            s.split(2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            2 / 0

if __name__ == '__main__':
    unittest.main()
```

> note: library vs framework: you use library in your code the way you want. framework is a structure that dictates you to follow it. (unittest, django are frameworks)

