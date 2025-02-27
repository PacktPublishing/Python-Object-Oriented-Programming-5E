"""
Python 3 Object-Oriented Programming Case Study

Chapter 4.
"""


class EvenOnly(list[int]):
    def append(self, value: int) -> None:
        match value:
            case int():
                pass
            case _:
                raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)


test_even_only = """
>>> e = EvenOnly()
>>> e.append("a string")
Traceback (most recent call last):
...
TypeError: Only integers can be added

>>> e.append(3)
Traceback (most recent call last):
...
ValueError: Only even numbers can be added
>>> e.append(2)
"""


test_even_only_missing_methods = """
To be complete, we need to make sure these don't work, also. 
>>> e = EvenOnly([1, 2, 3])
>>> e.extend([2, 3, 4])
>>> e[0] = 3
>>> e.insert(0, 5)
>>> e
[5, 3, 2, 3, 2, 3, 4]
"""

from typing import NoReturn


def never_returns() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"


test_never_returns = """
>>> never_returns()
Traceback (most recent call last):
...
    never_returns()
...
    raise Exception("This is always raised")
Exception: This is always raised

"""


def call_exceptor() -> None:
    print("call_exceptor starts here...")
    never_returns()
    print("an exception was raised...")
    print("...so these lines don't run")


test_call_exceptor = """
>>> call_exceptor()
Traceback (most recent call last):
...
    call_exceptor()
...
    never_returns()
...
    raise Exception("This is always raised")
Exception: This is always raised

"""


def handler() -> None:
    try:
        never_returns()
        print("Never executed")
    except Exception as ex:
        print(f"I caught an exception: {ex!r}")
    print("Executed after the exception")


test_handler = """
>>> handler()
I am about to raise an exception
I caught an exception: Exception('This is always raised')
Executed after the exception

"""


def funny_division(divisor: float) -> str | float:
    try:
        return 100 / divisor
    except ZeroDivisionError:
        return "Zero is not a good idea!"


test_funny_division = """
>>> print(funny_division(0))
Zero is not a good idea!
>>> print(funny_division(50.0))
2.0
>>> print(funny_division("hello"))
Traceback (most recent call last):
...
    print(funny_division("hello"))
          ^^^^^^^^^^^^^^^^^^^^^^^
...
    return 100 / divisor
           ~~~~^~~~~~~~~
TypeError: unsupported operand type(s) for /: 'int' and 'str'

"""


def funnier_division(divisor: int) -> str | float:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


test_funnier_division = """
>>> for val in (0, "hello", 50.0):
...     print(f"Testing {val!r}:", end=" ")
...     print(funnier_division(val))
... 
Testing 0: Enter a number other than zero
Testing 'hello': Enter a number other than zero
Testing 50.0: 2.0
>>> val = 13
>>> print(funnier_division(val))
Traceback (most recent call last):
...
    print(funnier_division(val))
          ^^^^^^^^^^^^^^^^^^^^^
...
    raise ValueError("13 is an unlucky number")
ValueError: 13 is an unlucky number

"""


def funniest_division(divisor: int) -> str | float:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise


test_funniest_division = """
>>> for val in (0, "hello", 50.0, 13):
...     print(f"Testing {val!r}:", end=" ")
...     print(funniest_division(val))
Traceback (most recent call last):
...
ValueError: 13 is an unlucky number

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
