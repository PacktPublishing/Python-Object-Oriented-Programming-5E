"""
Python 3 Object-Oriented Programming Case Study

Chapter 4, Expecting the Unexpected
"""

test_syntax_error = """
>>> print "hello world"
Traceback (most recent call last):
...
    print "hello world"
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""


test_more_exceptions = """
>>> x = 5 / 0
Traceback (most recent call last):
...
    x = 5 / 0
        ~~^~~
ZeroDivisionError: division by zero

>>> lst = [1,2,3]
>>> print(lst[3])
Traceback (most recent call last):
...
    print(lst[3])
          ~~~^^^
IndexError: list index out of range
>>> lst + 2
Traceback (most recent call last):
...
    lst + 2
    ~~~~^~~
TypeError: can only concatenate list (not "int") to list
>>> lst.add
Traceback (most recent call last):
...
    lst.add
AttributeError: 'list' object has no attribute 'add'

>>> d = {'a': 'hello'}
>>> d['b']
Traceback (most recent call last):
...
    d['b']
    ~^^^^^
KeyError: 'b'

>>> print(this_is_not_a_var)
Traceback (most recent call last):
...
    print(this_is_not_a_var)
          ^^^^^^^^^^^^^^^^^
NameError: name 'this_is_not_a_var' is not defined
"""


test_args = """
>>> try: 
...     raise ValueError("This is an argument") 
... except ValueError as e: 
...     print(f"The exception arguments were {e.args}") 
...
The exception arguments were ('This is an argument',)
"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
