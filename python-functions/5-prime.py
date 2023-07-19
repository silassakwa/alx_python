'''
Write a Python function called is_prime that takes a number as input and returns True if the number is prime, and False otherwise.
'''
#!/usr/bin/env python3
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
print(is_prime(25))
print(is_prime(2))
