"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""

import ecommerce.products

product_1 = ecommerce.products.Product("fore")

# or

from ecommerce.products import Product

product_2 = Product("main")

# or

from ecommerce import products

product_3 = products.Product("mizzen")

## Other Examples

from ecommerce import db

assert db is None  # Default.

test_1 = """
>>> import ecommerce.products
>>> product_1 = ecommerce.products.Product("fore")
>>> product_1.name
'fore'
"""

test_2 = """
>>> from ecommerce.products import Product
>>> product_2 = Product("main")
>>> product_2.name
'main'
"""

test_3 = """
>>> from ecommerce import products
>>> product_3 = products.Product("mizzen")
>>> product_3.name
'mizzen'
"""


__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
