"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

test_objs = """
>>> type("Hello, world!")
<class 'str'>
>>> type(42)
<class 'int'>
"""


test_a_string_variable = """
>>> a_string_variable = "Hello, world!"
>>> type(a_string_variable)
<class 'str'>
>>> a_string_variable = 42
>>> type(a_string_variable)
<class 'int'>
"""


test_odd = """
>>> def odd(n):
...     return n % 2 != 0
>>> odd(3)
True
>>> odd(4)
False

>>> odd("Hello, world!")
Traceback (most recent call last):
  File "/Users/slott/.local/share/uv/python/cpython-3.12.5-macos-x86_64-none/lib/python3.12/doctest.py", line 1368, in __run
    exec(compile(example.source, filename, "single",
  File "<doctest console_examples.__test__.test_odd[3]>", line 1, in <module>
    odd("Hello, world!")
  File "<doctest console_examples.__test__.test_odd[0]>", line 2, in odd
    return n % 2 != 0
           ~~^~~
TypeError: not all arguments converted during string formatting
"""


test_odd_hints = """
>>> def odd(n: int) -> bool:
...     return n % 2 != 0
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
