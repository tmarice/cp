
import fileinput
from collections import defaultdict


mapping = {
    'a': '2', 
    'b': '2',
    'c': '2',

    'd': '3', 
    'e': '3',
    'f': '3',

    'g': '4', 
    'h': '4',
    'i': '4',

    'j': '5', 
    'k': '5',
    'l': '5',

    'm': '6', 
    'n': '6',
    'o': '6',

    'p': '7', 
    'q': '7',
    'r': '7',
    's': '7',

    't': '8', 
    'u': '8',
    'v': '8',

    'w': '9', 
    'x': '9',
    'y': '9',
    'z': '9',
}


def convert(s):
    return "".join(mapping[c] for c in s)


def main():
    t9_dict = defaultdict(list)

    for i, line in enumerate(fileinput.input()):
        if i == 0:
            n, k = (int(x) for x in line.split())

        elif i <= n:
            t9_dict[convert(line.strip())].append(line.strip())

        else:
            r = t9_dict.get(line.strip())

            if r is None:
                print("EMPTY")
            else:
                print(" ".join(r))


if __name__ == "__main__":
    main()
