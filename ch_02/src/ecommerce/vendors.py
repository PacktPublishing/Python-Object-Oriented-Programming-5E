"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

import ecommerce.database

def some_code():
    """Create references to make the import look useful"""
    ecommerce.database

class Vendor:
    def __init__(self, name: str) -> None:
        self.name = name
