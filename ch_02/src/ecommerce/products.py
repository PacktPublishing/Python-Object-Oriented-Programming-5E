"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

import ecommerce.database as database

db_1 = database.Database("file:/path/to/data")

# OR

from .database import Database

db_2 = Database("file:/path/to/data")

# OR

from .database import Database as DB

db_3 = DB("file:/path/to/data")


from .database import Database, Query

from .contact.email import send_mail

def some_code():
    """Create references to make the import look useful"""
    Database
    DB
    Query
    send_mail

class Product:
    def __init__(self, name: str) -> None:
        self.name = name
