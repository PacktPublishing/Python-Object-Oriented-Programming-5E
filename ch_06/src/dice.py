"""
Python 3 Object-Oriented Programming Case Study

Chapter 6, Abstract Base Classes and Operator Overloading
"""
import abc
from collections.abc import Iterable
import random
from typing import cast, Any


class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"

    # A hint for one of the exercises.

    def __mul__(self, other: Any) -> "DDice":
        match other:
            case int():
                return DDice(type(self)) * other
            case _:
                return NotImplemented

    def __rmul__(self, other: Any) -> "DDice":
        """
        >>> random.seed(42)
        >>> d6 = D6()
        >>> x = 3*d6 + 2
        >>> x.total
        8
        """
        match other:
            case int():
                return other * DDice(type(self))
            case _:
                return NotImplemented


class D4(Die):
    def roll(self) -> None:
        self.face = random.choice((1, 2, 3, 4))


class D6(Die):
    def roll(self) -> None:
        self.face = random.randint(1, 6)


class D8(Die):
    def roll(self) -> None:
        self.face = int(random.random() * 8)


test_abc = """
>>> class Bad(Die):
...     def roll(self, a: int, b: int) -> float:
...         return (a+b)/2
>>> x = Bad()
Traceback (most recent call last):
...
    self.roll()
    ~~~~~~~~~^^
TypeError: Bad.roll() missing 2 required positional arguments: 'a' and 'b'

"""

test_die = """
>>> random.seed(42)
>>> dice = [D4(), D4(), D4()]
>>> faces = [d.face for d in dice]
>>> faces
[1, 1, 3]

>>> intelligence = [D6() for _ in range(3)]
>>> sum(d.face for d in intelligence)
6
>>> [d.face for d in intelligence]
[2, 2, 2]

>>> from collections import Counter
>>> distribution = Counter(D8().face for _ in range(1000))
>>> distribution
Counter({5: 139, 7: 130, 6: 128, 3: 125, 4: 125, 1: 121, 0: 116, 2: 116})
"""


class Dice(abc.ABC):
    def __init__(self, n: int, die_class: type[Die]) -> None:
        self.dice = [die_class() for _ in range(n)]

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice)


class SimpleDice(Dice):
    def roll(self) -> None:
        for d in self.dice:
            d.roll()


test_simple = """
>>> random.seed(42)
>>> sd = SimpleDice(6, D6)
>>> sd.roll()
>>> sd.total
23
"""


class YachtDice(Dice):
    def __init__(self) -> None:
        super().__init__(5, D6)
        self.saved: set[int] = set()

    def saving(self, positions: Iterable[int]) -> "YachtDice":
        if not all(0 <= n < 6 for n in positions):
            raise ValueError("Invalid position")
        self.saved = set(positions)
        return self

    def roll(self) -> None:
        for n, d in enumerate(self.dice):
            if n not in self.saved:
                d.roll()
        self.saved = set()

test_explore = """
>>> Die.__abstractmethods__
frozenset({'roll'})
>>> Die.roll.__isabstractmethod__
True
"""


test_yact = """
>>> random.seed(42)
>>> sd = YachtDice()
>>> sd.roll()
>>> sd.dice
[2, 2, 2, 6, 1]
>>> sd.saving([0, 1, 2]).roll()
>>> sd.dice
[2, 2, 2, 6, 6]
 
"""


class DieM(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"


class D4M(DieM):
    def roll(self) -> None:
        self.face = random.choice((1, 2, 3, 4))


test_die_meta = """
>>> random.seed(42)
>>> dice = [D4M(), D4M(), D4M()]
>>> faces = [d.face for d in dice]
>>> faces
[1, 1, 3]
>>> sum(faces)
5

"""


class DDice:
    def __init__(self, *die_class: type[Die]) -> None:
        self.classes = die_class
        self.dice = [dc() for dc in self.classes]
        self.adjust: int = 0

    def plus(self, adjust: int = 0) -> "DDice":
        self.adjust = adjust
        return self

    def roll(self) -> None:
        for d in self.dice:
            d.roll()

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice) + self.adjust

    def __repr__(self) -> str:
        rule = ", ".join(type(d).__name__ for d in self.dice)
        return f"DDice({rule}).plus({self.adjust})"

    def __add__(self, die_class: Any) -> "DDice":
        match die_class:
            case type() if issubclass(die_class, Die):
                new_classes = self.classes + (die_class,)
                new = DDice(*new_classes).plus(self.adjust)
                return new
            case int() as adj:
                new = DDice(*self.classes).plus(self.adjust + adj)
                return new
            case _:
                return NotImplemented

    def __radd__(self, die_class: Any) -> "DDice":
        match die_class:
            case type() if issubclass(die_class, Die):
                new_classes = (die_class,) + self.classes
                new = DDice(*new_classes).plus(self.adjust)
                return new
            case int() as adj:
                new = DDice(*self.classes).plus(self.adjust + adj)
                return new
            case _:
                return NotImplemented

    def __mul__(self, n: Any) -> "DDice":
        match n:
            case int():
                new_classes = self.classes * n
                return DDice(*new_classes).plus(self.adjust)
            case _:
                return NotImplemented

    __rmul__ = __mul__

    def __iadd__(self, die_class: Any) -> "DDice":
        match die_class:
            case type() if issubclass(die_class, Die):
                self.classes += (die_class,)
                self.dice = [dc() for dc in self.classes]
                return self
            case int() as adj:
                self.adjust += adj
                return self
            case _:
                return NotImplemented


test_ddice = """
>>> random.seed(42)
>>> r1 = DDice(D6) + D6 + D6
>>> r1.dice
[6, 3, 2]

>>> r2 = DDice(D6, D6, D6) + 2
>>> r2.total
15

>>> r3 = D6 + DDice(D6) + D6
>>> r3.dice
[4, 1, 1]

>>> r4 = 2 + DDice(D6, D6)
>>> r4.total
9

>>> d = 3*DDice(D6)
>>> d.roll()
>>> d.dice
[6, 6, 6]
>>> e = d + D6
>>> e.roll()
>>> e.dice
[5, 3, 1, 2]

>>> x = 3 * DDice(D6) + 2
>>> x.total
9
>>> f"{x.dice} + {x.adjust}"
'[2, 2, 3] + 2'
>>> repr(x)
'DDice(D6, D6, D6).plus(2)'

>>> old_id = id(x)
>>> x += 1
>>> x.total
10
>>> old_id == id(x)
True

>>> y = DDice(D6, D6)
>>> old_id = id(y)
>>> y += D6
>>> old_id == id(y)
True
>>> repr(y)
'DDice(D6, D6, D6).plus(0)'

>>> random.seed(1337)
>>> y = DDice(D6, D6)
>>> y += D6
>>> y += 2
>>> y.roll()
>>> y.dice
[5, 6, 2]
>>> y.total
15
"""


import logging
from functools import wraps
from typing import Any


class DieMeta(abc.ABCMeta):
    def __new__(
        cls: type,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> "DieMeta":
        if "roll" in namespace and not getattr(
            namespace["roll"], "__isabstractmethod__", False
        ):
            namespace.setdefault("logger", logging.getLogger(name))

            original_method = namespace["roll"]

            @wraps(original_method)
            def logged_roll(self: "DieLog") -> None:
                original_method(self)
                self.logger.info(f"Rolled {self.face}")

            namespace["roll"] = logged_roll
        new_object = cast(
            "DieMeta", abc.ABCMeta.__new__(cls, name, bases, namespace)
        )
        return new_object


class DieLog(metaclass=DieMeta):
    logger: logging.Logger

    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.face}"


class D6L(DieLog):
    def roll(self) -> None:
        """Some documentation on D6L"""
        self.face = random.randrange(1, 7)


test_d6l = """
>>> random.seed(42)
>>> d = D6L()
>>> d.face
6

"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
