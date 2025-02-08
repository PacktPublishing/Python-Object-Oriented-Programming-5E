"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

from typing import Any

from ..database import Database
from ..contact.email import send_mail


def payment() -> dict[str, Any]:
    db = Database("path/to/data")
    data = db.fetch("test_2")
    send_mail("example", "subject", f"{data}")
    return {"key": "test_2"}
