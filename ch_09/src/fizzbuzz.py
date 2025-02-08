"""
Python 3 Object-Oriented Programming

Chapter 9. The Intersection of Object-Oriented and Functional Programming
"""

from typing import Callable


def fizz(x: int) -> bool:
    return x % 3 == 0

def buzz(x: int) -> bool:
    return x % 5 == 0

def name_or_number(
        number: int,
        *tests: Callable[[int], bool]
) -> str:
    for t in tests:
        if t(number):
            return t.__name__
    return str(number)

test_name_or_number = """

>>> name_or_number(1, fizz)
'1'
>>> name_or_number(3, fizz)
'fizz'
>>> name_or_number(5, fizz)
'5'
>>> name_or_number(5, fizz, buzz)
'buzz'

>>> for i in range(1, 11):
...     print(name_or_number(i, fizz, buzz))
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
"""


### Using functions to patch a class

class A:
    def show_something(self) -> None:
        print("My class is A")

test_class_a = """

>>> a_object = A()
>>> a_object.show_something()
My class is A
"""

def patched_show_something() -> None:
    print("My class is NOT A")

test_patch = """
>>> a_object = A()
>>> a_object.show_something = patched_show_something
>>> a_object.show_something()
My class is NOT A

>>> b_object = A()
>>> b_object.show_something()
My class is A
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
