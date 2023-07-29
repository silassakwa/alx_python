#!/usr/bin/python3
"""
New class Square
"""
class Square:
    """
    Represents a square with a private instance attribute 'size' that stores the side length of the square.

    Attributes:
        __size (int): The side length of the square.

    Methods:
        __init__(self, size):
            Constructor method to initialize the Square object with the given size.

        get_size(self):
            Getter method to access the private 'size' attribute.

    Why is 'size' a private attribute?
    The size of a square is crucial for various computations like area, perimeter, etc. As the class builder, we must have
    control over the type and value of this attribute to ensure the square's integrity. By keeping 'size' private, we can
    prevent unintended modification and apply proper validation to maintain the consistency of the square.

    Note: This class does not currently provide setter methods for 'size', as shown in this documentation. 
    In practice, setter methods should be implemented to modify the private 'size' attribute in a controlled manner.
    """

    def __init__(self, size: int):
        """
        Initializes a Square object with the given side length.

        Parameters:
            size (int): The side length of the square. No type or value verification is performed during instantiation.

        Returns:
            None
        """
        self.__size = size

    def get_size(self):
        """
        Gets the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

# Test the Square class
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))  # Output: <class '__main__.Square'>
    print(my_square.__dict__)  # Output: {'_Square__size': 3}

    try:
        print(my_square.size)  # Output: 'Square' object has no attribute 'size'
    except AttributeError as e:
        print(e)

    try:
        print(my_square.get_size())  # Output: 3
    except AttributeError as e:
        print(e)