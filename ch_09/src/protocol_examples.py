"""
Python 3 Object-Oriented Programming

Chapter 9. The Intersection of Object-Oriented and Functional Programming
"""

test_len = """
>>> len([1, 2, 3, 4])
4
"""


from collections.abc import Sequence, Iterator
from typing import Any


class CustomSequence(Sequence[Any]):
    def __init__(self, arg: Sequence[Any]) -> None:
        self._list = arg
    def __len__(self) -> int:
        # This doesn't seem right, does it?
        return 5
    def __getitem__(self, index: int | slice) -> Any:
        return f"x{index}"


class FunkyBackwards(list[Any]):
    def __reversed__(self) -> Iterator[Any]:
        return iter("BACKWARDS!")


test_sequences = """
>>> generic = [1, 2, 3, 4, 5]
>>> custom = CustomSequence([6, 7, 8, 9, 10])
>>> funkadelic = FunkyBackwards([11, 12, 13, 14, 15])
>>> for sequence in generic, custom, funkadelic:
...     print(f"{sequence.__class__.__name__}: ", end="")
...     for item in reversed(sequence):
...         print(f"{item}, ", end="")
...     print()
list: 5, 4, 3, 2, 1, 
CustomSequence: x4, x3, x2, x1, x0, 
FunkyBackwards: B, A, C, K, W, A, R, D, S, !, 
"""


test_enumerate = """
>>> from pathlib import Path
>>> with open(Path.cwd() / "data" / "sample_data.md") as source:
...     for index, line in enumerate(source, start=1):
...         print(f"{index:3d}: {line.rstrip()}")
  1: # Python 3 Object-Oriented Programming
  2: 
  3: ## Chapter 9. The Intersection of Object-Oriented and Functional Programming
  4: 
  5: Some sample data to show how the `enumerate()` function works.
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
