"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""
from typing import Any


class Database:
    """The Database Implementation"""

    def __init__(self, connection: str | None = None) -> None:
        """Create a connection to a database."""
        self.connection = connection

    def fetch(self, key: str) -> dict[str, Any]:
        return {"key": key}


db: Database | None = None


def initialize_database(connection: str | None = None) -> None:
    global db
    if not db:
        db = Database(connection)


def get_database(connection: str | None = None) -> Database:
    global db
    if not db:
        db = Database(connection)
    return db



class Query:
    """A place-holder for a more sophistcated Query object."""

    def __init__(self, database: Database, collection: str) -> None:
        """Create a query for a database"""
        self.database = database
        self.collection = collection

test_db = """
>>> database = Database("file:/path/to/files")
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
