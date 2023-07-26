#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Calculate the sum
result = add(a, b)

# Print the result using string formatting
print("{} + {} = {}".format(a, b, result))