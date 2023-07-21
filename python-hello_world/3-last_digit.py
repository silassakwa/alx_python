#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

print("Last digit of {} is {} and is".format(number, last_digit), end=" \n")

if last_digit > 5:
    print("greater than 5",end="\n")
elif last_digit == 0:
    print("0",end="\n")
else:
    print("less than 6 and not 0",end="\n")