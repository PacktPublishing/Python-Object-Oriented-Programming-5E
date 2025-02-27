"""
Python 3 Object-Oriented Programming

Chapter 8. Python Data Structures
"""
import abc
from pathlib import Path
import time


class DirectoryVisitor(abc.ABC):
    queue_class: type["PathQueue"]

    def __init__(self, base: Path) -> None:
        self.queue = self.queue_class()
        self.queue.put(base)

    @abc.abstractmethod
    def file(self, path: Path) -> None:
        print(path)

    def visit(self) -> None:
        while not self.queue.empty():
            item = self.queue.get()
            if item.is_file():
                self.file(item)
            elif item.is_dir():
                if item.name.startswith("."):
                    continue
                if item.name == "__pycache__":
                    continue
                for sub_item in item.iterdir():
                    self.queue.put(sub_item)


from pathlib import Path


class ListQueue(list[Path]):
    """
    >>> lq = ListQueue()
    >>> lq.put(1)
    >>> lq.put(2)
    >>> lq.get() == 1
    True
    >>> lq.get() == 2
    True
    >>> lq.empty()
    True

    """

    def put(self, item: Path) -> None:
        self.append(item)

    def get(self) -> Path:
        return self.pop(0)

    def empty(self) -> bool:
        return len(self) == 0


from pathlib import Path
from typing import Deque


class DeQueue(Deque[Path]):
    """
    >>> dq = DeQueue()
    >>> dq.put(1)
    >>> dq.put(2)
    >>> dq.get() == 1
    True
    >>> dq.get() == 2
    True
    >>> dq.empty()
    True

    """

    def put(self, item: Path) -> None:
        self.append(item)

    def get(self) -> Path:
        return self.popleft()

    def empty(self) -> bool:
        return len(self) == 0


from pathlib import Path
import queue

class ThreadQueue(queue.Queue[Path]):
    """
    >>> tq = ThreadQueue()
    >>> tq.put(1)
    >>> tq.put(2)
    >>> tq.get() == 1
    True
    >>> tq.get() == 2
    True
    >>> tq.empty()
    True

    """

    pass


PathQueue = ListQueue | DeQueue | ThreadQueue


class WalkList(DirectoryVisitor):
    queue_class = ListQueue

    def file(self, path: Path) -> None:
        pass  # super().file(path)


class WalkDeque(DirectoryVisitor):
    queue_class = DeQueue

    def file(self, path: Path) -> None:
        pass  # super().file(path)


class WalkThread(DirectoryVisitor):
    queue_class = ThreadQueue

    def file(self, path: Path) -> None:
        pass  # super().file(path)


if __name__ == "__main__":
    performance: dict[str, float] = {}
    for cls in WalkList, WalkDeque, WalkThread:
        print(cls)
        start = time.perf_counter()
        for _ in range(100):
            walker = cls(Path.cwd())
            walker.visit()
        end = time.perf_counter()
        performance[cls.__name__] = (end - start) * 1000
        print()
    for cls_name, run_time in performance.items():
        print(f"{cls_name:10s} {run_time:5.2f}ms")
