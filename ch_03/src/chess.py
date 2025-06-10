"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 3, When Objects Are Alike.
"""
from __future__ import annotations
from enum import Enum
import abc

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

class ChessSet:
    pass

class Color(Enum):
    Red = 0xff0000
    Black = 0x000000

class Graphic:
    unicode_char: str
    def __init__(self, char: str) -> None:
        self.unicode_char = char

import abc

class Piece(abc.ABC):
    def __init__(self, set: ChessSet, color: Color, shape: Graphic) -> None:
        self.chess_set = set
        self.color = color
        self.shape = shape

    @abc.abstractmethod
    def move(self, board: Board, to: Position) -> None:
        ...

class Pawn(Piece):
    def move(self, board: Board, to: Position) -> None:
        """
        Remove self from the current position on the board.
        Update self in the new position on the board.
        """
        pass


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

test_piece = """
>>> s = ChessSet()
>>> p = Piece(s, Color.Black, Graphic("\N{BLACK CHESS PAWN}"))
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class Piece without an implementation for abstract method 'move'
"""

test_pawn = """
>>> s = ChessSet()
>>> pawn = Pawn(s, Color.Black, Graphic("\N{BLACK CHESS PAWN}"))
>>> pawn.shape.unicode_char
'♟'
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
