import sys

EXIT_FAILURE = 1


def whatis(num: int) -> str:
    if num % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


def main() -> None:
    args = sys.argv
    argc = len(args)

    if argc != 2:
        if argc > 2:
            print("AssertionError: Invalid number of arguments")
        sys.exit(EXIT_FAILURE)

    try:
        num = int(args[1])
    except ValueError:
        print("AssertionError: Argument is not an integer")
        sys.exit(EXIT_FAILURE)

    print(whatis(num))


main()
