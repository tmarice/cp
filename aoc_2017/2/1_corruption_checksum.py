
import sys


def get_checksum(rows):
    result = 0

    for row in rows:
        result += max(row) - min(row)

    return result


def main():
    lines = sys.stdin.readlines()

    rows = [[int(x) for x in row.strip().split()] for row in lines]

    print(get_checksum(rows))


if __name__ == "__main__":
    main()
