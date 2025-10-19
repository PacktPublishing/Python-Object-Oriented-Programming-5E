"""
An inspector to get object size.

For built-in collections, the size is clear.
For classes, however, it's a hair more complicated.

See https://code.activestate.com/recipes/577504-compute-memory-footprint-of-an-object-and-its-cont/

"""
from collections import deque
from collections.abc import Sequence, Mapping, Set, Callable, Iterator
import sys
from textwrap import shorten
from typing import Any


def get_object_size(some_object: Any, additional_types: Callable[[Any], int | None] | None = None, verbose: bool = False) -> int:
    """
    Computes the size of the given object.
    This expands on the recipe cited in the documentation for :py:func:`sys.getsizeof`.

    :param some_object: Any Python object.
    :param additional_types: A function that can return the size for an object for a type not handled here.
    :param verbose: True to print object information as the size is computed.
    :return: aggregate size of the object and all the related objects.

    The sizes are **highly** implementation specific.

    The types handled here are the built-in collections
    defined in :py:mod:`collections.abc`:
    ``str``, ``Sequence``, ``Set``, ``Mapping``.
    Additionally, this will look at any instance of class derived from :py:class:`object`,
    handling the default ``__dict__`` as well as ``__slots__``.

    >>> get_object_size("Hello, world!")
    54
    >>> get_object_size("!")
    42
    >>> get_object_size(list(range(10)))
    416
    """
    default_size = sys.getsizeof(0)
    seen = set()
    size = 0
    elements = deque([some_object])
    while elements:
        obj = elements.popleft()
        if id(obj) in seen:
            continue
        seen.add(id(obj))

        if verbose:
            print(f"{id(obj):8x} {type(obj)}, {shorten(repr(obj), 32)}", file=sys.stderr)

        size += sys.getsizeof(obj, default_size)
        match obj:
            case str():
                pass
            case Sequence() | Set():
                elements.extend(iter(obj))
            case Mapping():
                elements.extend(obj.keys())
                elements.extend(obj.values())
            case object() if hasattr(obj, '__dict__'):
                elements.extend(obj.__dict__.keys())
                elements.extend(obj.__dict__.values())
            case object() if hasattr(obj, '__slots__'):
                elements.extend(
                    getattr(obj, name)
                    for name in obj.__slots__
                    if hasattr(obj, name)
                )
            case _:
                if additional_types and (obj_size := additional_types(obj)) is not None:
                    size += obj_size
    return size
