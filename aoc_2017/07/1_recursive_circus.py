
import sys


def main():
    tree = {}

    for line in sys.stdin:
        line = line.strip()
        if "->" in line:
            left, right = line.split(" -> ")
        else:
            left, right = line, None

        name, weight = left.split()
        weight = int(weight[1:-1])

        if name not in tree:
            tree[name] = None

        if right:
            right_names = right.split(", ")

            for rn in right_names:
                tree[rn] = name

    for k, v in tree.items():
        if v is None:
            print(k)
            break


if __name__ == "__main__":
    main()
