

import fileinput

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text):
    for c in text:
        if c.isalpha():
            print(ALPHABET[ord(c) - ord("A") + 3], end='')
        else:
            print(c, end='')


def main():
    text = "".join(fileinput.input())

    encrypt(text)


if __name__ == "__main__":
    main()



