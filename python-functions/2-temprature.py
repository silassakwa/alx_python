#!/usr/bin/env python3
convert_to_celsius = __import__('2-temperature').convert_to_celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print(convert_to_celsius(71.5))