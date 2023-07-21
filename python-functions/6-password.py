def validate_password_length(password):
    return len(password) >= 8


# Test cases for password length validation
print(validate_password_length("Password123"))  # True
print(validate_password_length("abc123"))       # False
print(validate_password_length("12345678"))    # True
print(validate_password_length("short"))       # False