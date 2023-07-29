class Square:
    """
    Represents a square with a private instance attribute 'size' that stores the side length of the square.

    Attributes:
        __size (int): The side length of the square.

    Methods:
        __init__(self, size=0):
            Constructor method to initialize the Square object with the given size.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with the given side length.

        Args:
            size (int): The side length of the square. Default is 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

# Test the Square class
if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))  # Output: <class '__main__.Square'>
    print(my_square_1.__dict__)  # Output: {'_Square__size': 3}

    my_square_2 = Square()
    print(type(my_square_2))  # Output: <class '__main__.Square'>
    print(my_square_2.__dict__)  # Output: {'_Square__size': 0}

    try:
        print(my_square_1.size)  # Output: 'Square' object has no attribute 'size'
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