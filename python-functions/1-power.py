def power(a, b):
    result = a ** b
    length = len(str(result))
    return result, length

def print_result(result, length):
    print(result)
    print(f"({length} chars long)")

# Test the power function and print the results
result1, length1 = power(2, 2)
result2, length2 = power(98, 2)
result3, length3 = power(98, 0)
result4, length4 = power(100, -2)
result5, length5 = power(-4, 5)

print_result(result1, length1)
print_result(result2, length2)
print_result(result3, length3)
print_result(result4, length4)
print_result(result5, length5)