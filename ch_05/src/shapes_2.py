"""
Python 3 Object-Oriented Programming Case Study

Chapter 5, When to Use Object-Oriented Programming
"""
from math import hypot


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)


class Polygon:
    def __init__(self) -> None:
        self.vertices: list[Point] = []

    def add_point(self, point: Point) -> None:
        self.vertices.append(point)

    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)


test_polygon = """
>>> square = Polygon()
>>> square.add_point(Point(1,1))
>>> square.add_point(Point(1,2))
>>> square.add_point(Point(2,2))
>>> square.add_point(Point(2,1))
>>> square.perimeter()
4.0

"""


from collections.abc import Iterable


class Polygon_2:
    def __init__(self, vertices: Iterable[Point] | None = None) -> None:
        self.vertices = list(vertices) if vertices else []

    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)


test_polygon_2 = """
>>> square = Polygon_2(
... [Point(1,1), Point(1,2), Point(2,2), Point(2,1)]
... )
>>> square.perimeter()
4.0

"""


type Pair = tuple[float, float]
type Point_or_Tuple = Point | Pair


class Polygon_3:
    def __init__(
            self,
            vertices: Iterable[Point_or_Tuple] | None = None
    ) -> None:
        self.vertices: list[Point] = []
        for pt_tup in vertices or []:
            self.vertices.append(
                self.make_point(pt_tup)
            )

    @staticmethod
    def make_point(item: Point_or_Tuple) -> Point:
        match item:
            case Point() as pt:
                return pt
            case (float() | int(), float() | int()) as tup:
                return Point(*tup)
            case _:
                raise TypeError(
                    f"unexpected {type(item)}: {item!r}"
                )

    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)



test_polygon_3 = """
>>> square_explicit = Polygon_3(
... [Point(1,1), Point(1,2), Point(2,2), Point(2,1)]
... )
>>> square_explicit.perimeter()
4.0

>>> square_implicit = Polygon_3(
... [(1,1), (1,2), (2,2), (2,1)]
... )
>>> square_implicit.perimeter()
4.0

"""

test_complex_polygon_3 = """
>>> square_complex = Polygon_3(
... [(1, 1), (1, 1+1j), (1+1j, 1+1j), (1+1j, 1)]
... )
Traceback (most recent call last):
...
TypeError: unexpected <class 'tuple'>: (1, (1+1j))
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
