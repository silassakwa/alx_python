#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

if __name__ == "__main__":
    try:
        my_square_1 = Square(-2)
        if my_square_1.size < 0:
            raise ValueError("size must be >= 0")
    except TypeError:
        print("size must be an integer")
    except ValueError as e:
        print(e)
    else:

        print(my_square_1.size)

