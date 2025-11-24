import sys
import string


def get_input() -> str:
    """
    Get input from command line argument or prompt user for input.

    :return: Description
    :rtype: str
    """

    text = ""
    if len(sys.argv) == 1 or not sys.argv[1]:
        text = input("What is the text to write? ")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("AssertionError.")
        sys.exit(1)

    return text


def print_count(text: str) -> None:
    """
    Count and print the number of upper case letters, lower case letters,
    punctuation characters, digits and spaces in the given text.

    :param text: Description
    :type text: str
    """
    categories = [
        ("Upper", str.isupper),
        ("Lower", str.islower),
        ("Punct", lambda c: c in string.punctuation),
        ("Digit", str.isdigit),
        ("Space", str.isspace),
    ]

    counts = {name: 0 for name, _ in categories}

    for c in text:
        for name, fn_check in categories:
            if fn_check(c):
                counts[name] += 1
                break

    for name, count in counts.items():
        print(f"{name}: {count}")


def main():
    """
    Main function to execute the program logic.
    """

    print_count(get_input())


if __name__ == "__main__":
    main()
