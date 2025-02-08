"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

class Database:
    """The Database Implementation"""
    def __init__(self, connection: str | None = None) -> None:
        """Create a connection to a database."""
        pass

database = Database("file:/path/to/database")


test_db = """
>>> assert database is not None
"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
