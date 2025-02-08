"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

class Position:
    def __init__(self, file: str, rank: str) -> None:
        self.file = file
        self.rank = rank

class Board:
    def __init__(self) -> None:
        self.positions: dict[tuple[str, str], Position] = {}
        for file in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            for rank in ('1', '2', '3', '4', '5', '6', '7', '8'):
                self.positions[file, rank] = Position(file, rank)


test_pos = """
>>> p = Position("a", "1")
>>> f"{p.file}{p.rank}"
'a1'
"""

test_board = """
>>> b = Board()
>>> len(b.positions)
64
>>> p = b.positions["a", "1"]
>>> f"{p.file}{p.rank}"
'a1'
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
