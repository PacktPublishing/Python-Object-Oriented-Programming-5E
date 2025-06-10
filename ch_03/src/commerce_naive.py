"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 3, When Objects Are Alike
"""
## Extending built-ins

from __future__ import annotations

class ContactList(list["Contact"]):
    def search(self, name: str) -> list[Contact]:
        """All Contacts with name that contains the name parameter's value."""
        matching_contacts: list[Contact] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

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


class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )


class Order:
    pass


test_contact = """
Needed to reset the class *after* a previous test: 
>>> Contact.all_contacts = ContactList()

>>> c1 = Contact("John A", "johna@example.net")
>>> c2 = Contact("John B", "johnb@sloop.net")
>>> c3 = Contact("Jenna C", "cutty@sark.io")
>>> Contact.all_contacts.search('John')
[Contact('John A', 'johna@example.net'), Contact('John B', 'johnb@sloop.net')]

>>> [c.name for c in Contact.all_contacts.search('John')]
['John A', 'John B']
"""

test_list_demo = """
>>> [] == list()
True
"""


class LongNameDict(dict[str, int]):
    def longest_key(self) -> str | None:
        """In effect, max(self, key=len), but less obscure"""
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


test_longnamedict = """
>>> articles_read = LongNameDict()
>>> articles_read['lucy'] = 42
>>> articles_read['c_c_phillips'] = 6
>>> articles_read['steve'] = 7
>>> articles_read.longest_key()
'c_c_phillips'
>>> max(articles_read, key=len)
'c_c_phillips'
"""

## Overriding and super

class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone

class Friend_S(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone


test_friends = """
>>> f = Friend("Dusty", "Dusty@private.com", "555-1212")
>>> f
Friend('Dusty', 'Dusty@private.com')

>>> fs = Friend_S("Dusty", "Dusty@private.com", "555-1212")
>>> fs
Friend_S('Dusty', 'Dusty@private.com')
"""


class Friend_S2(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}, {self.phone!r}"
            f")"
        )

test_friends_2 = """
>>> f = Friend("Dusty", "Dusty@private.com", "555-1212")
>>> f
Friend('Dusty', 'Dusty@private.com')

>>> fs = Friend_S2("Dusty", "Dusty@private.com", "555-1212")
>>> fs
Friend_S2('Dusty', 'Dusty@private.com', '555-1212')
"""

## Multiple Inheritance


from typing import Protocol

class Emailable(Protocol):
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email=}")
        # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    pass


test_emailable_contact = """
Needed to reset the class *after* a previous test: 
>>> Contact.all_contacts = ContactList()

>>> e = EmailableContact("John B", "johnb@sloop.net")
>>> Contact.all_contacts
[EmailableContact('John B', 'johnb@sloop.net')]
>>> e.send_mail("Hello, test e-mail here")
Sending mail to self.email='johnb@sloop.net'
"""

## Multiple inheritance -- naive version


class AddressHolder:
    def __init__(
            self,
            street: str,
            city: str,
            state: str,
            code: str
    ) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend_A(Contact, AddressHolder):
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        street: str,
        city: str,
        state: str,
        code: str,
    ) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone


test_naive_friend_a = """
>>> naif = Friend_A("Naif", "naif@badidea.com", "555-1212", "1212 Mockingbird Lane", "W. Addams", "MA", "12345")
>>> naif.phone
'555-1212'

"""



__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
