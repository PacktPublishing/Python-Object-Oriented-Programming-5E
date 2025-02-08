"""
Python 3 Object-Oriented Programming Case Study

Chapter 6, Abstract Base Classes and Operator Overloading
"""
from collections.abc import Iterable, Hashable, Mapping
from typing import cast, Any

type DictInit = (
    Iterable[tuple[Hashable, Any]]
    | Mapping[Hashable, Any]
    | None
)


class NoDupdict(dict[Hashable, Any]):
    def __setitem__(self, key: Hashable, value: Any) -> None:
        if key in self:
            raise ValueError(f"duplicate {key!r}")
        super().__setitem__(key, value)

    def __init__(self, init: DictInit = None, **kwargs: Any) -> None:
        match init:
            case Mapping():
                super().__init__(init, **kwargs)
            case Iterable():
                for k, v in cast(Iterable[tuple[Hashable, Any]], init):
                    self[k] = v
            case None:
                super().__init__(**kwargs)
            case _:
                super().__init__(init, **kwargs)


test_nd_1 = """
>>> from collections.abc import Hashable
>>> from typing import Any

>>> class NoDupDict(dict):
...     def __setitem__(self, key, value) -> None:
...         if key in self:
...             raise ValueError(f"duplicate {key!r}")
...         super().__setitem__(key, value)

>>> nd = NoDupdict()
>>> nd["a"] = 1
>>> nd["a"] = 2
Traceback (most recent call last):
  ...
  File "<doctest examples.md[10]>", line 1, in <module>
    nd["a"] = 2
  File "<doctest examples.md[7]>", line 4, in __setitem__
    raise ValueError(f"duplicate {key!r}")
ValueError: duplicate 'a'
"""

test_nd_2 = """
Doesn't work -- Arguments created a standard dict first

>>> NoDupdict({"a": 42, "a": 3.14})
{'a': 3.14}
"""

test_nd_3 = """
>>> NoDupdict([("a", 42), ("a", 3.14)])
Traceback (most recent call last):
  ...
  File "<doctest examples.md[10]>", line 1, in <module>
    nd["a"] = 2
  File "<doctest examples.md[7]>", line 4, in __setitem__
    raise ValueError(f"duplicate {key!r}")
ValueError: duplicate 'a'

"""


test_nd_4 = """
Doesn't work -- update() doesn't rely on __setitem__()

>>> d_1 = NoDupdict([("a", 42), ("b", 3.14)])
>>> d_2 = NoDupdict([("a", ~42)])
>>> d_1.update(d_2)
>>> d_1
{'a': -43, 'b': 3.14}

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
