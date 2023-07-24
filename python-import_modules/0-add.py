# Importing the add function from add_0.py
from add_0 import add

# Assigning values to variables a and b
a = 1
b = 2

# Printing the result using string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
if __name__ == "__main__":
    