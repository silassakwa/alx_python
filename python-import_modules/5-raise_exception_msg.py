def raise_exception_msg(message=""):
    raise NameError(message)


#!/usr/bin/python3

if __name__ == "__main__":
    raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg

    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)