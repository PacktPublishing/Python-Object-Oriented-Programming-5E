"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""

test_syntax = """
>>> s_1 = {
...     'symbol': 'GOOG',
...     'current': 1245.21,
...     'range': (1252.64, 1245.18)
... }
>>> s_2 = dict(
...     symbol='GOOG',
...     current=1245.21,
...     range=(1252.64, 1245.18)
... )

"""


from decimal import Decimal
from typing import TypedDict

class Range(TypedDict):
    low: Decimal
    high: Decimal

class Stock(TypedDict):
    symbol: str
    current: Decimal
    range: Range

test_td_syntax = """
>>> s_td = Stock(
...     symbol='GOOG',
...     current=Decimal('166.57'),
...     range=Range(low=Decimal('129.40'), high=Decimal('193.31'))
... )

"""

from decimal import Decimal
import datetime
from typing import TypedDict, NotRequired

class StockN(TypedDict):
    symbol: str
    name: NotRequired[str]
    current: Decimal
    range: Range
    date: NotRequired[datetime.date]

test_not_required = """
>>> s = StockN(symbol="RIMM", name=None, current=Decimal('123.45'),
...     range=Range(low=Decimal('1.00'), high=Decimal('200.00')))
>>> s
{'symbol': 'RIMM', 'name': None, 'current': Decimal('123.45'), 'range': {'low': Decimal('1.00'), 'high': Decimal('200.00')}}
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
