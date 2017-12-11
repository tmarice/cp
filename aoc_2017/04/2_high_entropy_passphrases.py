
import sys


def main():
    passphrases = sys.stdin.readlines()

    valid_passphrases = 0
    for pp in passphrases:
        words = pp.split()
        if len(words) == len(set([frozenset(w) for w in words])):
            valid_passphrases += 1

    print(valid_passphrases)


if __name__ == "__main__":
    main()
