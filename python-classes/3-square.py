class Square:
    """
    Represents a square with a given size.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0):
            Initializes a new Square object with the specified size.

        area(self):
            Calculates and returns the area of the square.

        my_print(self):
            Prints the square using '#' characters in the standard output.
            If the size is 0, it prints an empty line.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int, optional): The size of the square's sides. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square's sides.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square's sides.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size * self.size

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, it prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)