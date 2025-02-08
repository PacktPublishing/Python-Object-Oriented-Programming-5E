"""
Python 3 Object-Oriented Programming Case Study

Chapter 5, When to Use Object-Oriented Programming
"""
from math import hypot

type Point = tuple[float, float]


def distance(p_1: Point, p_2: Point) -> float:
    return hypot(p_1[0] - p_2[0], p_1[1] - p_2[1])


type Polygon = list[Point]


def perimeter(polygon: Polygon) -> float:
    pairs = zip(polygon, polygon[1:] + polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)


test_hack_script = """
>>> square = [(1,1), (1,2), (2,2), (2,1)]

>>> from math import hypot

>>> def distance(p_1, p_2):
...     return hypot(p_1[0] - p_2[0], p_1[1] - p_2[1])

>>> def perimeter(polygon):
...     pairs = zip(polygon, polygon[1:] + polygon[:1])
...     return sum(
...         distance(p1, p2) for p1, p2 in pairs
...     )

>>> perimeter(square)
4.0

"""

test_functions = """
>>> square = [(1,1), (1,2), (2,2), (2,1)]
>>> perimeter(square)
4.0
"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
