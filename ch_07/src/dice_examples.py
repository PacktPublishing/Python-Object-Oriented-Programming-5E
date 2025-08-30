"""
Python 3 Object-Oriented Programming Case Study

Chapter 7, Python Type Hints.
"""

from random import randint

def roll_dice(sides: list[int] | None = None) -> list[int]:
    dice_mix = sides if sides is not None else [6, 6]
    return [randint(1, s) for s in dice_mix]


test_roll_dice = """
>>> import random
>>> random.seed(42)

>>> roll_dice([6, 6, 6])
[6, 1, 1]
>>> roll_dice()
[6, 3]

"""


from random import randint

def roll_ndice(
        dice: int | list[int] | None = None,
        faces: int | None = None
    ) -> list[int]:
    match dice:
        case int() as n:
            dice_mix = n * [faces or 6]
        case None:
            if faces is None:
                dice_mix = [6, 6]
            else:
                dice_mix = [faces]
        case list() as dice_mix:
            assert faces is None, "faces must be None when dice is a list"
        case _:
            raise TypeError(f"can't parse {dice=!r}")
    return [randint(1, s) for s in dice_mix]


test_roll_ndice = """
>>> import random
>>> random.seed(42)

>>> roll_ndice([6, 6, 6])
[6, 1, 1]
>>> roll_ndice()
[6, 3]
>>> roll_ndice(2, 6)
[2, 2]
>>> roll_ndice(3)
[2, 6, 1]
>>> roll_ndice(faces=20)
[18]

"""

from typing import overload

@overload
def roll_ndice2(
    dice: list[int] | None
) -> list[int]:
    ...

@overload
def roll_ndice2(
    dice: int | None = None,
    faces: int | None = None
) -> list[int]:
    ...

def roll_ndice2(
        dice: int | list[int] | None = None,
        faces: int | None = None
    ) -> list[int]:
    # The body goes here...
    match dice:
        case int() as n:
            dice_mix = n * [faces or 6]
        case None:
            if faces is None:
                dice_mix = [6, 6]
            else:
                dice_mix = [faces]
        case list() as dice_mix:
            assert faces is None, "faces must be None when dice is a list"
        case _:
            raise TypeError(f"can't parse {dice=!r}")
    return [randint(1, s) for s in dice_mix]


test_roll_ndice2 = """
>>> import random
>>> random.seed(42)

>>> roll_ndice2([6, 6, 6])
[6, 1, 1]
>>> roll_ndice2()
[6, 3]
>>> roll_ndice2(2, 6)
[2, 2]
>>> roll_ndice2(3)
[2, 6, 1]
>>> roll_ndice2(faces=20)
[18]

"""

from collections.abc import Iterable
from typing import overload


@overload
def roll_ndice3(
    dice: Iterable[int] | None
) -> list[int]:
    ...

@overload
def roll_ndice3(
    dice: int | None = None,
    faces: int = 2
) -> list[int]:
    ...

def roll_ndice3(
        dice: int | Iterable[int] | None = None,
        faces: int | None = None
    ) -> list[int]:
    match dice:
        case int() as n:
            dice_mix = n * [faces or 6]
        case None:
            if faces is None:
                dice_mix = [6, 6]
            else:
                dice_mix = [faces]
        case Iterable() as dice_mix:
            assert faces is None, "faces must be None when dice is a list"
        case _:
            raise TypeError(f"can't parse {dice=!r}")
    return [randint(1, s) for s in dice_mix]

test_roll_ndice3 = """
>>> import random
>>> random.seed(42)

>>> roll_ndice3([6, 6, 6])
[6, 1, 1]
>>> roll_ndice3()
[6, 3]
>>> roll_ndice3(2, 6)
[2, 2]
>>> roll_ndice3(3)
[2, 6, 1]
>>> roll_ndice3(faces=20)
[18]

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
