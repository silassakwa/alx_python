#!/usr/bin/python3
"""
New class Square
"""


class Square:
    def __init__(self, size):
        self.__size = size

# Test the Square class
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))  # Output: <class '__main__.Square'>
    print(my_square.__dict__)  # Output: {'_Square__size': 3}

    try:
        print(my_square.size)  # Output: 'Square' object has no attribute 'size'
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)  # Output: 'Square' object has no attribute '__size'
    except Exception as e:
        print(e)