#!/usr/bin/python3
Square = __import__('3-square').Square

# Create a square with size 89
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# Set the size of the square to 3 and print its area and size
my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    # Try to set the size of the square to "5 feet"
    # This will raise a TypeError and be caught by the except block
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    # Print the exception message if the size is not an integer
    print(e)