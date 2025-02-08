"""
Python 3 Object-Oriented Programming

Chapter 6, Abstract Base Classes and Operator Overloading
"""
from contextlib import AbstractContextManager
from io import StringIO
import sys
from typing import Literal
from types import TracebackType


class DebuggingOnly(AbstractContextManager["DebuggingOnly"]):
    """Similar to contextlib.redirect_stdout"""

    def __enter__(self) -> "DebuggingOnly":
        self.previous = sys.stdout
        self.buffer = StringIO()
        sys.stdout = self.buffer
        return self

    def __exit__(
        self,
        exc_class: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[False]:
        sys.stdout = self.previous
        if exc:
            print(f"--EX-->{exc!r}")
            for line in self.buffer.getvalue().splitlines():
                print(f"       {line}")
        return False

