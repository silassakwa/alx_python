def validate_password(password):
    if len(password) < 8:
        return False

    is_password_uppercase = False
    is_password_lowercase = False
    has_digit = False

    for character in password:
        if character.isupper():
            is_password_uppercase = True
        elif character.islower():
            is_password_lowercase = True
        elif character.isdigit():
            has_digit = True

    return is_password_uppercase and is_password_lowercase and has_digit

print(validate_password("silasSakwa "))  # Output: True
