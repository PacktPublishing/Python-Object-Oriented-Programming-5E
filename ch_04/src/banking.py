"""
Python 3 Object-Oriented Programming Case Study

Chapter 4, Expecting the Unexpected
"""

class InvalidWithdrawal_1(ValueError):
    pass

test_exception_1 = """
>>> raise InvalidWithdrawal_1("You don't have $50 in your account")
Traceback (most recent call last):
...
banking.InvalidWithdrawal_1: You don't have $50 in your account
"""

from decimal import Decimal


class InvalidWithdrawal(ValueError):
    def __init__(self, balance: Decimal, amount: Decimal) -> None:
        super().__init__(f"account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance

    def overage(self) -> Decimal:
        return self.amount - self.balance

test_exception_2 = """
>>> raise InvalidWithdrawal(Decimal('28.63'), Decimal('42.00'))
Traceback (most recent call last):
...
banking.InvalidWithdrawal: account doesn't have $42.00
"""


def do_transfer(balance: Decimal, transfer: Decimal) -> Decimal:
    if transfer > balance:
        raise InvalidWithdrawal(balance, transfer)
    balance -= transfer
    return balance

test_transfer = """
>>> balance = Decimal('28.63')
>>> transfer = Decimal('42.00')
>>> try:
...     new_balance = do_transfer(balance, transfer)
... except InvalidWithdrawal as ex:
...     print("I'm sorry, but your withdrawal is " 
...           "more than your balance by " 
...           f"${ex.overage()}")
...
I'm sorry, but your withdrawal is more than your balance by $13.37
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}

