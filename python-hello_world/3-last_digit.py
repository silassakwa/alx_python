# 3-last_digit.py
import random

# Generate a random signed number between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Check the value of the last digit and print the result
print(f"The string Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")