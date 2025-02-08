"""
Python 3 Object-Oriented Programming Case Study

Chapter 6, Abstract Base Classes and Operator Overloading
"""

test_container = """
>>> from collections.abc import Container
>>> Container.__abstractmethods__ 
frozenset({'__contains__'})
"""

test_help = """
>>> from collections.abc import Container

>>> help(Container.__contains__)
Help on function __contains__ in module collections.abc:
<BLANKLINE>
__contains__(self, x)
<BLANKLINE>
"""

test_pathlib = """
>>> from pathlib import Path
>>> home = Path.home()
>>> home / ".cargo" / "bin" / "uv"
PosixPath('/Users/slott/.cargo/bin/uv')
"""

test_base_dict = """
>>> d = {"a": 42, "a": 3.14}
>>> d
{'a': 3.14}

>>> {1: "one", True: "true"}
{1: 'true'}

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
