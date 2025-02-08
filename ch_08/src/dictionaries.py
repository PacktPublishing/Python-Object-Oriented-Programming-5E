"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""
import datetime
from decimal import Decimal
from typing import NamedTuple

test_dict_homogenous_example = """
>>> from dataclasses import dataclass
>>> @dataclass
... class Stock:
...     symbol: str
...     price: Decimal
...     high: Decimal
...     low: Decimal

>>> stocks = {
...     "GOOG": Stock("GOOG", Decimal('166.57'), high=Decimal('193.31'), low=Decimal('129.40')),
...     "MSFT": Stock("MSFT", Decimal('110.41'), high=Decimal('110.45'), low=Decimal('109.84')),
... }
"""

class DailyQuote(NamedTuple):
    symbol: str
    date: datetime.date
    price: Decimal

some_source_of_daily_quotes = [
    DailyQuote("AAPL", datetime.date(2024, 11, 22), Decimal('226.20')),
    DailyQuote("AAPL", datetime.date(2024, 1, 1), Decimal('237.49')),
    DailyQuote("AAPL", datetime.date(2024, 2, 2), Decimal('164.075')),
    DailyQuote("GOOG", datetime.date(2024, 3, 3), Decimal('1826.77')),
    DailyQuote("GOOG", datetime.date(2024, 4, 4), Decimal('1847.20')),
]

test_setdefault = """
>>> summary: dict[str, list[DailyQuote]] = {}
>>> for dq in some_source_of_daily_quotes:
...     summary.setdefault(dq.symbol, list())
...     summary[dq.symbol].append(dq)
...
[]
...
>>> from pprint import pprint
>>> pprint(summary)
{'AAPL': [DailyQuote(symbol='AAPL', date=datetime.date(2024, 11, 22), price=Decimal('226.20')),
          DailyQuote(symbol='AAPL', date=datetime.date(2024, 1, 1), price=Decimal('237.49')),
          DailyQuote(symbol='AAPL', date=datetime.date(2024, 2, 2), price=Decimal('164.075'))],
 'GOOG': [DailyQuote(symbol='GOOG', date=datetime.date(2024, 3, 3), price=Decimal('1826.77')),
          DailyQuote(symbol='GOOG', date=datetime.date(2024, 4, 4), price=Decimal('1847.20'))]}

"""

test_defaultdict = """
>>> from collections import defaultdict

>>> summary: defaultdict[str, list[DailyQuote]] = defaultdict(list)
>>> for dq in some_source_of_daily_quotes:
...     summary[dq.symbol].append(dq)
...
>>> from pprint import pprint
>>> pprint(summary)
defaultdict(<class 'list'>,
            {'AAPL': [DailyQuote(symbol='AAPL', date=datetime.date(2024, 11, 22), price=Decimal('226.20')),
                      DailyQuote(symbol='AAPL', date=datetime.date(2024, 1, 1), price=Decimal('237.49')),
                      DailyQuote(symbol='AAPL', date=datetime.date(2024, 2, 2), price=Decimal('164.075'))],
             'GOOG': [DailyQuote(symbol='GOOG', date=datetime.date(2024, 3, 3), price=Decimal('1826.77')),
                      DailyQuote(symbol='GOOG', date=datetime.date(2024, 4, 4), price=Decimal('1847.20'))]})

"""


test_counter = """
>>> from collections import Counter

>>> frequency = Counter()
>>> for dq in some_source_of_daily_quotes:
...     frequency[dq.symbol] += 1

>>> frequency
Counter({'AAPL': 3, 'GOOG': 2})

>>> from collections import Counter

>>> symbols = (dq.symbol for dq in some_source_of_daily_quotes)
>>> frequency = Counter(symbols)

>>> frequency
Counter({'AAPL': 3, 'GOOG': 2})

"""

class StockQuoteSummary(dict[str, list[DailyQuote]]):
    def __missing__(self, symbol: str) -> list[DailyQuote]:
        self[symbol] = list()
        return self[symbol]
    def by_date(self, symbol: str) -> list[DailyQuote]:
        return sorted(self[symbol], key=lambda dq: dq.date)

test_stock_quote_summary = """
>>> summary = StockQuoteSummary()
>>> for dq in some_source_of_daily_quotes:
...    summary[dq.symbol].append(dq)

>>> for symbol in summary:
...    print(summary.by_date(symbol))
[DailyQuote(symbol='AAPL', date=datetime.date(2024, 1, 1), price=Decimal('237.49')), DailyQuote(symbol='AAPL', date=datetime.date(2024, 2, 2), price=Decimal('164.075')), DailyQuote(symbol='AAPL', date=datetime.date(2024, 11, 22), price=Decimal('226.20'))]
[DailyQuote(symbol='GOOG', date=datetime.date(2024, 3, 3), price=Decimal('1826.77')), DailyQuote(symbol='GOOG', date=datetime.date(2024, 4, 4), price=Decimal('1847.20'))]
"""

test_hash = """
>>> x = 2020
>>> y = 2305843009213695971
>>> hash(x) == hash(y)
True
>>> x == y
False
"""

## Some older examples.

def letter_frequency(sentence: str) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


test_lf_1 = """
>>> txt = "A quick brown fox jumps over the lazy dog"
>>> letter_frequency(txt)
{'A': 1, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'e': 2, 't': 1, 'h': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}

"""

from collections import defaultdict


def letter_frequency_2(sentence: str) -> defaultdict[str, int]:
    frequencies: defaultdict[str, int] = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


test_lf_2 = """
>>> txt = "A quick brown fox jumps over the lazy dog"
>>> letter_frequency_2(txt)
defaultdict(<class 'int'>, {'A': 1, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'e': 2, 't': 1, 'h': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1})

>>> import collections
>>> lf = collections.defaultdict(lambda: "Unknown", letter_frequency_2(txt))
>>> lf["A"]
1
>>> lf[":"]
'Unknown'

"""

from collections import Counter


def letter_frequency_3(sentence: str) -> Counter[str]:
    return Counter(sentence)


test_lf_3 = """
>>> txt = "A quick brown fox jumps over the lazy dog"
>>> letter_frequency_3(txt)
Counter({' ': 8, 'o': 4, 'u': 2, 'r': 2, 'e': 2, 'A': 1, 'q': 1, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 't': 1, 'h': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1})

"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
