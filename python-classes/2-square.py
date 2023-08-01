class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor method for Square class.
            Initializes a square object with the given size.
        area(self): Calculates and returns the area of the square.

    Raises:
        TypeError: If the input size is not an integer.
        ValueError: If the input size is less than 0.
    """

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  # size of the square

    def area(self):
        """calculate and print the area of the square"""
        return self.__size ** 2
   #!/usr/bin/python3
"""
2-main.py - A script to demonstrate the Square class functionality.

This script demonstrates the usage of the Square class defined in the module 2-square.py.
It creates instances of the Square class with different sizes and calculates their areas.

Classes:
    None

Functions:
    None
"""

# Importing the Square class from the module 2-square.py
Square = __import__('2-square').Square


# Create a Square object with size 3 and calculate its area
my_square_1 = Square(3)
# Accessing the 'size' attribute of the Square object and handling the exception if it does not exist
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)
# Create another Square object with size 5 and calculate its area
my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))