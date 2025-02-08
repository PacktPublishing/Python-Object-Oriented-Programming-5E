"""
Python 3 Object-Oriented Programming

Chapter 9. The Intersection of Object-Oriented and Functional Programming
"""
from typing import Any


def show_args(arg1: Any, arg2: Any, arg3: Any="THREE") -> str:
    return f"{arg1=}, {arg2=}, {arg3=}"

test_unpacking = """
Unpacking a sequence

>>> some_args = range(3)
>>> show_args(*some_args)
'arg1=0, arg2=1, arg3=2'

Unpacking a dict

>>> more_args = {
... "arg1": "ONE",
... "arg2": "TWO"}
>>> show_args(**more_args)
"arg1='ONE', arg2='TWO', arg3='THREE'"

"""

test_packing = """
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 11, 'c': 3}
>>> z = {**x, **y}
>>> z
{'a': 1, 'b': 11, 'c': 3}

"""

import heapq
import time
from typing import Optional, Callable
from dataclasses import dataclass, field

type Callback = Callable[[int], None]


@dataclass(frozen=True, order=True)
class Task:
    """
    Definition of a task to be performed at an interval after the Scheduler starts.
    The scheduled time is interpreted by the Scheduler class, generally seconds.
    The task is any function that will be given the scheduler's notion of elapsed time.

    If provided, the delay is a reschedule delay. The limit is the number of
    times the task can be run, default is once only.
    """

    scheduled: int
    callback: Callback = field(compare=False)
    delay: int = field(default=0, compare=False)
    limit: int = field(default=1, compare=False)

    def repeat(self, current_time: int) -> Optional["Task"]:
        """
        If the limit is > 1, this task can be run again.
        Create a new Task object with the time at which it should be repeated.
        """
        if self.delay > 0 and self.limit > 2:
            return Task(
                current_time + self.delay,
                self.callback,
                self.delay,
                self.limit - 1,
            )
        elif self.delay > 0 and self.limit == 2:
            return Task(
                current_time + self.delay,
                self.callback,
            )
        else:
            return None


class Scheduler:
    """
    Schedule tasks for execution.
    Use :meth:`enter` to put tasks into the queue.
    Use :meth:`run` to start processing.
    Currently, this uses default time.sleep() which means ``after`` and ``delay`` are
    in seconds.
    """

    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def enter(
        self,
        after: int,
        task: Callback,
        delay: int = 0,
        limit: int = 1,
    ) -> None:
        new_task = Task(after, task, delay, limit)
        heapq.heappush(self.tasks, new_task)

    def run(self) -> None:
        current_time = 0
        while self.tasks:
            next_task = heapq.heappop(self.tasks)
            if (delay := next_task.scheduled - current_time) > 0:
                time.sleep(delay)
            current_time = next_task.scheduled
            next_task.callback(current_time)
            if again := next_task.repeat(current_time):
                heapq.heappush(self.tasks, again)


import datetime


def format_time(message: str) -> None:
    now = datetime.datetime.now()
    print(f"{now:%I:%M:%S}: {message}")


def one(timer: float) -> None:
    format_time("Called One")


def two(timer: float) -> None:
    format_time("Called Two")


def three(timer: float) -> None:
    format_time("Called Three")


class Repeater:
    def __init__(self) -> None:
        self.count = 0

    def four(self, timer: float) -> None:
        self.count += 1
        format_time(f"Called Four: {self.count}")


class Repeater_2:
    def __init__(self) -> None:
        self.count = 0

    def __call__(self, timer: float) -> None:
        self.count += 1
        format_time(f"Called Four: {self.count}")


test_workers = """
>>> from unittest.mock import Mock, patch
>>> expected_date = datetime.datetime(2019, 10, 26, 11, 12, 13)
>>> mock_method = Mock(return_value=expected_date)
>>> with patch('datetime.datetime', now=mock_method):
...     one(42)
...     two(42)
...     three(55)
11:12:13: Called One
11:12:13: Called Two
11:12:13: Called Three

>>> rpt = Repeater()
>>> with patch('datetime.datetime', now=mock_method):
...     rpt.four(42)
...     rpt.four(43)
...     rpt.four(44)
11:12:13: Called Four: 1
11:12:13: Called Four: 2
11:12:13: Called Four: 3

>>> rpt2 = Repeater_2()
>>> with patch('datetime.datetime', now=mock_method):
...     rpt2(42)
...     rpt2(43)
...     rpt2(44)
11:12:13: Called Four: 1
11:12:13: Called Four: 2
11:12:13: Called Four: 3

"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}

if __name__ == "__main__":
    s = Scheduler()
    s.enter(1, one)
    s.enter(2, one)
    s.enter(2, two)
    s.enter(4, two)
    s.enter(3, three)
    s.enter(6, three)
    repeater = Repeater()
    s.enter(5, repeater.four, delay=1, limit=5)
    s.run()

    s2 = Scheduler()
    s2.enter(5, Repeater_2(), delay=1, limit=5)
    s2.run()
