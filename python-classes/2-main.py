
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