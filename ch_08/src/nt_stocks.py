"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""
from decimal import Decimal
from typing import NamedTuple

class Stock(NamedTuple):
    symbol: str
    current: Decimal
    high: Decimal
    low: Decimal

test_stock = """
>>> Stock("AAPL", Decimal('226.20'), Decimal('237.49'), Decimal('164.075'))
Stock(symbol='AAPL', current=Decimal('226.20'), high=Decimal('237.49'), low=Decimal('164.075'))

>>> s2 = Stock("AAPL", Decimal('226.20'), high=Decimal('237.49'), low=Decimal('164.075'))
>>> s2
Stock(symbol='AAPL', current=Decimal('226.20'), high=Decimal('237.49'), low=Decimal('164.075'))

>>> s2.high
Decimal('237.49')
>>> s2[2]
Decimal('237.49')
>>> symbol, current, high, low = s2
>>> high
Decimal('237.49')

>>> s2.current = Decimal('229.87')
Traceback (most recent call last):
  ...
    s2.current = Decimal('229.87')
    ^^^^^^^^^^
AttributeError: can't set attribute
"""

test_tuple_with_list = """
>>> t = ("Relayer", ["Gates of Delirium", "Sound Chaser"])
>>> t[1].append("To Be Over")
>>> t
('Relayer', ['Gates of Delirium', 'Sound Chaser', 'To Be Over'])

>>> hash(t)
Traceback (most recent call last):
  ...
    hash(t)
TypeError: unhashable type: 'list'
"""

class StockM(NamedTuple):
    symbol: str
    current: Decimal
    high: Decimal
    low: Decimal

    @property
    def middle(self) -> Decimal:
        return (self.high + self.low) / 2

test_s_m_property = """
>>> s_m = StockM("AAPL", Decimal('226.20'), high=Decimal('237.49'), low=Decimal('164.075'))
>>> s_m.middle
Decimal('200.7825')

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
