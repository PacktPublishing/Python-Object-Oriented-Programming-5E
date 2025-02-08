"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    current: Decimal
    high: Decimal
    low: Decimal


test_stock = """
>>> s = Stock("AAPL", Decimal('226.20'), Decimal('237.49'), Decimal('164.075'))
>>> s
Stock(symbol='AAPL', current=Decimal('226.20'), high=Decimal('237.49'), low=Decimal('164.075'))

>>> s.current
Decimal('226.20')
>>> s.current = Decimal('229.87')
>>> s
Stock(symbol='AAPL', current=Decimal('229.87'), high=Decimal('237.49'), low=Decimal('164.075'))

>>> s.unexpected_attribute = 'allowed'
>>> s.unexpected_attribute
'allowed'

>>> stock2 = Stock("AAPL", Decimal('229.87'), high=Decimal('237.49'), low=Decimal('164.075'))
>>> s == stock2
True
"""


@dataclass
class StockDefaults:
    name: str
    current: Decimal = Decimal('0.00')
    high: Decimal = Decimal('0.00')
    low: Decimal = Decimal('0.00')


test_stock_defaults = """
>>> StockDefaults("GOOG")
StockDefaults(name='GOOG', current=Decimal('0.00'), high=Decimal('0.00'), low=Decimal('0.00'))
>>> StockDefaults("GOOG", Decimal('166.57'), Decimal('193.31'), Decimal('129.40'))
StockDefaults(name='GOOG', current=Decimal('166.57'), high=Decimal('193.31'), low=Decimal('129.40'))

"""


@dataclass(order=True)
class StockOrdered:
    name: str
    current: Decimal = Decimal('0.00')
    high: Decimal = Decimal('0.00')
    low: Decimal = Decimal('0.00')


test_stock_ordered = """
>>> stock_ordered1 = StockOrdered("GOOG", Decimal('166.57'), Decimal('193.31'), Decimal('129.40'))
>>> stock_ordered2 = StockOrdered("GOOG")
>>> stock_ordered3 = StockOrdered("GOOG", Decimal('142.45'), high=Decimal('151.85'), low=Decimal('84.95'))

>>> stock_ordered1 < stock_ordered2
False
>>> stock_ordered1 > stock_ordered2
True
>>> from pprint import pprint
>>> pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))
[StockOrdered(name='GOOG',
              current=Decimal('0.00'),
              high=Decimal('0.00'),
              low=Decimal('0.00')),
 StockOrdered(name='GOOG',
              current=Decimal('142.45'),
              high=Decimal('151.85'),
              low=Decimal('84.95')),
 StockOrdered(name='GOOG',
              current=Decimal('166.57'),
              high=Decimal('193.31'),
              low=Decimal('129.40'))]

"""



test_stock_defaultdict = """
>>> import collections
>>> from dataclasses import dataclass
>>> from decimal import Decimal
>>> @dataclass
... class Prices:
...     current: Decimal = Decimal('0.00')
...     high: Decimal = Decimal('0.00')
...     low: Decimal = Decimal('0.00')
...
>>> Prices() 
Prices(current=Decimal('0.00'), high=Decimal('0.00'), low=Decimal('0.00'))

>>> portfolio = collections.defaultdict(Prices)
>>> portfolio["GOOG"]
Prices(current=Decimal('0.00'), high=Decimal('0.00'), low=Decimal('0.00'))
>>> portfolio["AAPL"] = Prices(Decimal('226.20'), Decimal('237.49'), Decimal('164.075'))

>>> from pprint import pprint
>>> pprint(portfolio)
defaultdict(<class 'dc_stocks.Prices'>,
            {'AAPL': Prices(current=Decimal('226.20'),
                            high=Decimal('237.49'),
                            low=Decimal('164.075')),
             'GOOG': Prices(current=Decimal('0.00'),
                            high=Decimal('0.00'),
                            low=Decimal('0.00'))})


>>> by_month = collections.defaultdict(
...     lambda : collections.defaultdict(Prices)
... )
>>> by_month["APPL"]["Jan"] = Prices(Decimal('226.20'), Decimal('237.49'), Decimal('164.075'))
>>> by_month
defaultdict(<function <lambda> at ...>, {'APPL': defaultdict(<class 'dc_stocks.Prices'>, {'Jan': Prices(current=Decimal('226.20'), high=Decimal('237.49'), low=Decimal('164.075'))})})

"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
