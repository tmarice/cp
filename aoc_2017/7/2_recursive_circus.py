
import sys


def main():
    tree = {}
    children = {}
    weights = {}

    for line in sys.stdin:
        line = line.strip()
        if "->" in line:
            left, right = line.split(" -> ")
        else:
            left, right = line, None

        name, weight = left.split()
        weight = int(weight[1:-1])

        weights[name] = weight

        if name not in tree:
            tree[name] = None

        if right:
            right_names = right.split(", ")

            children[name] = right_names

            for rn in right_names:
                tree[rn] = name
        else:
            children [name] = None

    for k, v in tree.items():
        if v is None:
            root = k
            break

    cum_weights = {}

    def cum_ws(node):
        if children[node] is None:
            cum_weights[node] = weights[node]
        else:
            cum_weights[node] = weights[node] + sum(cum_ws(c) for c in children[node])

        return cum_weights[node]

    cum_ws(root)

    def balance(node, diff):
        if children[node] is None:
            return weights[node] + diff

        if len(children[node]) == 1:
            return balance(children[node][0], diff)

        children_weights = sorted([(cum_weights[c], c) for c in children[node]])

        if children_weights[0][0] < children_weights[1][0]:
            return balance(children_weights[0][1], children_weights[1][0] - children_weights[0][0])
        elif children_weights[-1][0] > children_weights[-2][0]:
            return balance(children_weights[-1][1], children_weights[-2][0] - children_weights[-1][0])
        else:
            return weights[node] + diff

    d = balance(root, 0)

    print(d)


if __name__ == "__main__":
    main()
