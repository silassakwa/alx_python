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
   