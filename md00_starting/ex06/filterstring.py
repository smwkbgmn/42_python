import sys
import ft_filter


def main():
    """
    Main function to filter words longer than N characters from a given string.
    """
    try:
        # Validate number of arguments
        if len(sys.argv) != 3:
            raise AssertionError("wrong number of arguments")

        # Validate N is an integer
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("second argument is not an integer")

        # Take the input string and filter words
        text = sys.argv[1]
        words = text.split()
        result = ft_filter.filter(lambda word: len(word) > n, words)

        print(list(result))

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
