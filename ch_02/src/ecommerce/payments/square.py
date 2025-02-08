"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""
from ..database import Database

class SomeClass:
    d = Database("file:/path/to/data")


test_2 = """
>>> db = Database("path/to/data")
>>> db.fetch("test_2")
{'key': 'test_2'}
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
