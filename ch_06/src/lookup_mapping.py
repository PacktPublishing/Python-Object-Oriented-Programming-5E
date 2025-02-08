"""
Python 3 Object-Oriented Programming

Chapter 6, Abstract Base Classes and Operator Overloading
"""
import bisect
from collections.abc import Iterator, Iterable, Mapping
from typing import Protocol, Any, overload, cast


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __ne__(self, other: Any) -> bool:
        ...

    def __le__(self, other: Any) -> bool:
        ...

    def __lt__(self, other: Any) -> bool:
        ...

    def __ge__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...


# type BaseMapping = Mapping[Comparable, Any]


class Lookup(Mapping[Comparable, Any]):
    @overload
    def __init__(self, source: Iterable[tuple[Comparable, Any]]) -> None:
        ...

    @overload
    def __init__(self, source: "Mapping[Comparable, Any]") -> None:
        ...

    def __init__(
        self,
        source: Any = None,
    ) -> None:
        sorted_pairs: list[tuple[Comparable, Any]]
        match source:
            case Iterable() as an_iter:
                # Assume it's pairs.
                sorted_pairs = sorted(
                    cast(Iterable[tuple[Comparable, Any]], an_iter)
                )
            case Mapping() as a_map:
                sorted_pairs = sorted(a_map.items())
            case _:
                sorted_pairs = []
        self.key_list: list[Comparable] = [p[0] for p in sorted_pairs]
        self.value_list: list[Any] = [p[1] for p in sorted_pairs]

    def __len__(self) -> int:
        return len(self.key_list)

    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)

    def __contains__(self, key: object) -> bool:
        index = bisect.bisect_left(
            self.key_list,
            cast(Comparable, key)
        )
        return key == self.key_list[index]

    def __getitem__(self, key: Comparable) -> Any:
        index = bisect.bisect_left(self.key_list, key)
        if key == self.key_list[index]:
            return self.value_list[index]
        raise KeyError(key)


test_lookup = """
>>> x = Lookup(
...     [
...         ["z", "Zillah"],
...         ["a", "Amy"],
...         ["c", "Clara"],
...         ["b", "Basil"],
...     ]
... )

>>> x["c"]
'Clara'
"""

test_not_a_dict = """
>>> x = Lookup(
...     [
...         ["z", "Zillah"],
...         ["a", "Amy"],
...         ["c", "Clara"],
...         ["b", "Basil"],
...     ]
... )

>>> x["m"] = "Maud"
Traceback (most recent call last):
  ...
  File "<doctest lookup_mapping.__test__.test_not_a_dict[1]>", line 1, in <module>
    x["m"] = "Maud"
TypeError: 'Lookup' object does not support item assignment

"""

test_dict_init_examples = """
>>> x = dict({"a": 42, "b": 7, "c": 6})
>>> y = dict([("a", 42), ("b", 7), ("c", 6)])
>>> x == y
True

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
