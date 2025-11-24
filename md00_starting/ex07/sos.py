import sys


def encode(text: str) -> str:
    """
    Encode the input text into Morse code.

    :param text: Description
    :type text: str
    :return: Description
    :rtype: str
    """

    MORSE_CODE = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        " ": "/"
    }

    morse = ""
    for i, c in enumerate(text.lower()):
        morse += MORSE_CODE[c]
        morse += " " if i < len(text) - 1 else ""

    return morse


def valid(text: str) -> bool:
    """
    Validate that the input text contains only alphanumeric characters and spaces.

    :param text: Description
    :type text: str
    :return: Description
    :rtype: bool
    """
    for c in text:
        if not c.isalnum() and c != ' ':
            return False
    return True


def main():
    """
    Main function to handle command-line input and output the Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Exactly one argument is required")

        text = (sys.argv[1]).lower()

        if not valid(text):
            raise AssertionError(
                "Input should only contain alphanumeric characters and spaces"
            )

        print(encode(text))

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
