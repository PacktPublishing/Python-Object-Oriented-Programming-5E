"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 3, When Objects Are Alike
"""

import abc


class MediaLoader(abc.ABC):
    ext: str

    @abc.abstractmethod
    def play(self) -> None:
        ...


test_abstractions = """
>>> MediaLoader.__abstractmethods__ == frozenset({'play'})
True

"""

test_concrete_subclasses = """
>>> class Wav(MediaLoader): 
...     pass 
... 
>>> x = Wav() 
Traceback (most recent call last):
...
    x = Wav()
TypeError: Can't instantiate abstract class Wav without an implementation for abstract method 'play'

>>> class Ogg(MediaLoader): 
...     ext = '.ogg' 
...     def play(self) -> None: 
...         pass 
... 
>>> o = Ogg() 

"""

# Exposed here so mypy can examine this, also.


class Ogg(MediaLoader):
    ext = ".ogg"

    def play(self) -> None:
        pass


o = Ogg()

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
