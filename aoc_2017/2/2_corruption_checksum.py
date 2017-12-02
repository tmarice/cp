
import sys


def get_checksum(rows):
    result = 0

    for row in rows:
        end = len(row)
        for i in range(end - 1):
            for j in range(i + 1, end):
                if row[i] % row[j] == 0:
                    result += row[i] // row[j]
                elif row[j] % row[i] == 0:
                    result += row[j] // row[i]

    return result


def main():
    lines = sys.stdin.readlines()

    rows = [[int(x) for x in row.strip().split()] for row in lines]

    print(get_checksum(rows))


if __name__ == "__main__":
    main()
