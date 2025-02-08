"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""


class MyFirstClass:
    pass


test_first_class = """
>>> a = MyFirstClass()
>>> b = MyFirstClass()
>>> print(a)
<first_class.MyFirstClass object at ...>
>>> print(b)
<first_class.MyFirstClass object at ...>

>>> a is b
False
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
