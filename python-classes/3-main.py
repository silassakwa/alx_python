
# Import the Square class from 3-square.py
Square = __import__('3-square').Square
# Create a Square object 'my_square' with size 89
my_square = Square(89)

# Print the area and size of 'my_square' using area() method and size property
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

# Change the size of 'my_square' to 3
my_square.size = 3

# Print the updated area and size of 'my_square' after the size change
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    # Try to set the size of 'my_square' to a non-integer value ("5 feet")
    my_square.size = "5 feet"

    # Since 'size' should only accept integers, this will raise a TypeError
    # The error will be caught in the 'except' block
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    # Print the error message raised by the setter
    print(e)