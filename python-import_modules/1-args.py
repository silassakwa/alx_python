import sys

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    print("{} argument{}:".format(num_args, "s" if num_args != 1 else ""), end="")
    if num_args == 0:
        print(" .")
    else:
        print()
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()