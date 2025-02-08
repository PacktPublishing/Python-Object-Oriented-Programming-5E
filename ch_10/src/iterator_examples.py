"""
Python 3 Object-Oriented Programming

Chapter 10. The Iterator Pattern

Expects HASHSEED=42
"""


from collections.abc import Iterable
from typing import Any


class DumbIterator:
    def __init__(self, collection: "DumbCollection") -> None:
        self.collection = collection
        self.index = 0
    def next(self) -> Any:
        r = self.collection.data[self.index]
        self.index += 1
        return r
    def done(self) -> bool:
        return self.index == len(self.collection.data)

class DumbCollection:
    def __init__(self, source: Iterable[Any]) -> None:
        self.data = list(source)
    def iterator(self) -> DumbIterator:
        return DumbIterator(self)

def iter_while(some_collection: DumbCollection) -> None:
    iterator = some_collection.iterator()
    while not iterator.done():
        item = iterator.next()
        # do something with the item from some_collection...
        print(item)

test_iter_while = """
>>> collection = DumbCollection(["1", "1", "2", "3"])
>>> iter_while(collection)
1
1
2
3
"""

test_strings_1 = """
>>> input_strings = ["1", "5", "28", "131", "3"]
 
>>> output_integers = [] 
>>> for num in input_strings: 
...    output_integers.append(int(num)) 
>>> output_integers
[1, 5, 28, 131, 3]

"""

test_strings_2 = """
>>> input_strings = ["1", "5", "28", "131", "3"]
 
>>> output_integers = [int(num) for num in input_strings] 
>>> output_integers
[1, 5, 28, 131, 3]

"""

test_strings_3 = """
>>> input_strings = ["1", "5", "28", "131", "3"]
>>> output_integers = [int(num) for num in input_strings if len(num) < 3]
>>> output_integers
[1, 5, 28, 3]

"""

test_path = """
>>> from pathlib import Path

>>> chapter = Path.cwd()
>>> paths = [path.relative_to(chapter) 
...     for path in chapter.glob("src/*.py") 
...     if ">>>" in path.read_text()
... ]
>>> paths.sort()

>>> import sys
>>> assert (
...     paths == [Path('src/iterator_examples.py'), Path('src/iterator_protocol.py'), Path('src/log_analysis.py'), ]
... ), f"Invalid {paths!r} for {sys.platform!r}"

>>> source_path = Path('src') / 'iterator_protocol.py'
>>> with source_path.open() as source:
...     examples = [line.rstrip() 
...         for line in source 
...         if ">>>" in line]
>>> examples
[">>> iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')", '>>> iterator = iter(iterable)', '>>> while True:', '>>> for i in iterable:', '>>> iterator = iter(iterable)', '>>> for i in iter(iterator):']

>>> source_path = Path('src') / 'iterator_protocol.py'
>>> with source_path.open() as source:
...     examples = [(number, line.rstrip()) 
...         for number, line in enumerate(source, start=1) 
...         if ">>>" in line]
>>> examples
[(35, ">>> iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')"), (36, '>>> iterator = iter(iterable)'), (37, '>>> while True:'), (53, '>>> for i in iterable:'), (66, '>>> iterator = iter(iterable)'), (67, '>>> for i in iter(iterator):')]

>>> import doctest
>>> import iterator_protocol
>>> test_finder = doctest.DocTestFinder()
>>> [test.name for test in test_finder.find(iterator_protocol)]
['iterator_protocol', 'iterator_protocol.__test__.test_iterable']

"""

### Set and dictionary comprehensions


from typing import NamedTuple


class Book(NamedTuple):
    author: str
    title: str
    genre: str

test_set_dict_comprehension = """
>>> books = [
...     Book("Pratchett", "Nightwatch", "fantasy"),
...     Book("Pratchett", "Thief Of Time", "fantasy"),
...     Book("Le Guin", "The Dispossessed", "scifi"),
...     Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
...     Book("Jemisin", "The Broken Earth", "fantasy"),
...     Book("Turner", "The Thief", "fantasy"),
...     Book("Phillips", "Preston Diamond", "western"),
...     Book("Phillips", "Twice Upon A Time", "scifi"),
... ]

>>> fantasy_authors = {b.author for b in books if b.genre == "fantasy"}
>>> fantasy_authors
{'Jemisin', 'Le Guin', 'Pratchett', 'Turner'}

>>> fantasy_titles = {b.title: b for b in books if b.genre == "fantasy"}
>>> fantasy_titles
{'Nightwatch': Book(author='Pratchett', title='Nightwatch', genre='fantasy'), 'Thief Of Time': Book(author='Pratchett', title='Thief Of Time', genre='fantasy'), 'A Wizard Of Earthsea': Book(author='Le Guin', title='A Wizard Of Earthsea', genre='fantasy'), 'The Broken Earth': Book(author='Jemisin', title='The Broken Earth', genre='fantasy'), 'The Thief': Book(author='Turner', title='The Thief', genre='fantasy')}
>>> fantasy_titles['Nightwatch']
Book(author='Pratchett', title='Nightwatch', genre='fantasy')


"""

## Generator expressions

test_generator = """

>>> from pathlib import Path

>>> full_log_path = Path.cwd() / "data" / "sample.log"
>>> warning_log_path = Path.cwd() / "data" / "warnings.log"

>>> with full_log_path.open() as source:
...     warning_lines = (line for line in source if "WARN" in line)
...     with warning_log_path.open('w') as target:
...         for line in warning_lines:
...             _ = target.write(line)

>>> with warning_log_path.open() as warnings:
...     for line in warnings:
...         print(line.rstrip())
Apr 05, 2021 20:03:53 WARNING This is a warning. It could be serious.
Apr 05, 2021 20:03:59 WARNING Another warning sent.
Apr 05, 2021 20:04:35 WARNING Warnings should be heeded.
Apr 05, 2021 20:04:41 WARNING Watch for warnings.

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
