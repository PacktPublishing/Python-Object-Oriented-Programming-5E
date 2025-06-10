"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 3, When Objects Are Alike
"""
from __future__ import annotations
from typing import ClassVar


class Contact:
   all_contacts: ClassVar[list[Contact]] = []

   def __init__(self, name: str, email: str) -> None:
       self.name = name
       self.email = email
       Contact.all_contacts.append(self)

   def __repr__(self) -> str:
       return (
           f"{self.__class__.__name__}("
           f"{self.name!r}, {self.email!r}"
           f")"
      )


test_contact = """
>>> c_1 = Contact("Dusty", "dusty@example.com")
>>> c_2 = Contact("Steve", "steve@itmaybeahack.com")
>>> Contact.all_contacts
[Contact('Dusty', 'dusty@example.com'), Contact('Steve', 'steve@itmaybeahack.com')]
"""


class Supplier(Contact):
   def order(self, order: "Order") -> None:
       print(
           "If this were a real system we would send "
           f"'{order}' order to '{self.name}'"
       )


class Order:
    pass


test_supplier = """
>>> c = Contact("Some Body", "somebody@example.net")
>>> s = Supplier("Sue Plier", "supplier@example.net")
>>> print(c.name, c.email, s.name, s.email)
Some Body somebody@example.net Sue Plier supplier@example.net
>>> from pprint import pprint
>>> pprint(c.all_contacts)
[Contact('Dusty', 'dusty@example.com'),
 Contact('Steve', 'steve@itmaybeahack.com'),
 Contact('Some Body', 'somebody@example.net'),
 Supplier('Sue Plier', 'supplier@example.net')]
>>> c.order("I need pliers")
Traceback (most recent call last):
...
AttributeError: 'Contact' object has no attribute 'order'
>>> s.order("I need pliers")
If this were a real system we would send 'I need pliers' order to 'Sue Plier'
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
