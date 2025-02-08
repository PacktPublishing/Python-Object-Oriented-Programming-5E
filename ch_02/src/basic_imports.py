"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

import random

def dice1() -> tuple[int, int]:
    return (
        random.randint(1, 6), random.randint(1, 6)
    )

test_dice_1 = """
>>> random.seed(42)
>>> dice1()
(6, 1)
"""

from random import randint

def dice2() -> tuple[int, int]:
    return (
        randint(1, 6), randint(1, 6)
    )

test_dice_2 = """
>>> random.seed(42)
>>> dice2()
(6, 1)
"""


from random import randint as rng

def dice3() -> tuple[int, int]:
    return (
        rng(1, 6), rng(1, 6)
    )

test_dice_3 = """
>>> random.seed(42)
>>> dice3()
(6, 1)
"""

from random import seed, Random

def dice4() -> tuple[int, int]:
    seed()
    rng = Random()
    rng.seed(42)
    return (
        rng.randint(1, 6), rng.randint(1, 6)
    )

test_dice_4 = """
>>> random.seed(42)
>>> dice4()
(6, 1)
"""


__test__ = {name: case for name, case in globals().items() if
            name.startswith("test_")}
