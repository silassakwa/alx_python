def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
print(convert_to_celsius(100))  # Output: 37.77777777777778
print(convert_to_celsius(-40))  # Output: -40.0
print(convert_to_celsius(-459.67))  # Output: -273.15
print(convert_to_celsius(32))  # Output: 0.0
print(convert_to_celsius(98.6))  # Output: 37.0