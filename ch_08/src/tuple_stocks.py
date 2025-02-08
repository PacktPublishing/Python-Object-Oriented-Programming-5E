"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""

test_stock = """
>>> stock = "AAPL", 226.20, 237.49, 164.075
>>> stock2 = ("AAPL", 226.20, 237.49, 164.075)

>>> import datetime
>>> def middle(stock, date):
...     symbol, current, high, low = stock
...     return (((high + low) / 2), date)
>>> middle(("AAPL", 226.20, 237.49, 164.075), datetime.date(2024, 11, 22))
(200.7825, datetime.date(2024, 11, 22))

>>> stock = "AAPL", 226.20, 237.49, 164.075
>>> high = stock[2]
>>> high
237.49

>>> stock[1:3]
(226.2, 237.49)

>>> def high(quote):
...     symbol, current, high, low = quote
...     return high
>>> high(stock)
237.49

"""


test_syntax = """
>>> a = 42,
>>> a
(42,)
"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
