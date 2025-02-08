"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.


"""


def odd(n: int) -> bool:
    return n % 2 != 0


def main() -> None:
    print(odd("Hello, world!"))


if __name__ == "__main__":
    main()
