import random

# Generate a random signed number between -100 and 100 (inclusive)
number = random.randint(-100, 100)

# Check if the number is positive, negative, or zero and print the result
if number > 0:
    print(f"{number}: is positive")
elif number == 0:
    print(f"{number}: is zero")
else:
    print(f"{number}: is negative")