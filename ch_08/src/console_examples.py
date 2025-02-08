"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""
import sys

if sys.version_info[:2] == (3, 13):
    test_object_3_13 = """
>>> o = object()
>>> o.x = 5
Traceback (most recent call last):
...
    o.x = 5
    ^^^
AttributeError: 'object' object has no attribute 'x' and no __dict__ for setting new attributes
"""

if sys.version_info[:2] == (3, 12):
    test_object_3_12 = """
>>> o = object()
>>> o.x = 5
Traceback (most recent call last):
...
    o.x = 5
    ^^^
AttributeError: 'object' object has no attribute 'x'
"""

test_class = """
>>> class MyObject: 
...     pass 

>>> m = MyObject()
>>> m.x = "hello"
>>> m.x
'hello'
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
