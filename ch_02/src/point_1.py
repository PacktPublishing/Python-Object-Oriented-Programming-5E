"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""


class Point:
    def reset(self) -> None:
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)


test_manual_self = """
>>> p = Point()
>>> Point.reset(p)  # Works, but...
>>> print(p.x, p.y)
0 0
"""


test_no_self = """
>>> class Point:
...     def reset():
...         pass
...
>>> p = Point()
>>> p.reset()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Point.reset() takes 0 positional arguments but 1 was given
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
