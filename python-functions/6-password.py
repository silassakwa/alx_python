def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check if the password contains spaces
    if " " in password:
        return False

    # If all checks pass, return True
    return True

#!/usr/bin/env python3
validate_password = __import__('6-password').validate_password

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
