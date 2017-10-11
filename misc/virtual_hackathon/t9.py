
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

    n, k = (int(x) for x in input().split())

    for _ in range(n):
        w = input().strip()
        t9_dict[convert(w)].append(w)

    for _ in range(k):
        w = input().strip()

        r = t9_dict.get(w)

        if r is None:
            print("EMPTY")
        else:
            print(" ".join(sorted(r)))


if __name__ == "__main__":
    main()
