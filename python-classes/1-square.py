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
        print(type(my_square_1))  # Output: <class '__main__.Square'>
        print(my_square_1.__dict__)  # Output: {'size': 3}

    my_square_2 = Square()
    print(type(my_square_2))  # Output: <class '__main__.Square'>
    print(my_square_2.__dict__)  # Output: {'size': 0}

    try:
        print(my_square_1.size)  # Output: 3
    except AttributeError as e:
        print(e)

    try:
        print(my_square_1.__size)  # Output: 'Square' object has no attribute '__size'
    except AttributeError as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)  # Output: size must be an integer

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)  # Output: size must be >= 0
