"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""
from __future__ import annotations
import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: Point) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)



test_point = """
>>> point1 = Point(0, 0)
>>> point2 = Point(0, 0)

>>> point1.reset()
>>> point2.move(5, 0)
>>> print(point2.calculate_distance(point1))
5.0
>>> assert point2.calculate_distance(point1) == point1.calculate_distance(
...    point2
... )
>>> point1.move(3, 4)
>>> print(point1.calculate_distance(point2))
4.47213595499958
>>> print(point1.calculate_distance(point1))
0.0
"""


test_init = """
>>> point = Point(3, 5)
>>> print(point.x, point.y)
3 5

>>> point = Point()
Traceback (most recent call last):
...
TypeError: Point.__init__() missing 2 required positional arguments: 'x' and 'y'

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
