def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result

if __name__ == "__main__":
    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))