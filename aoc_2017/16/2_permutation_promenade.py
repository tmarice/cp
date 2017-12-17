
from collections import deque


def simulate(order, ops):

    for op in ops:
        if op[0] == 's':
            n = int(op[1:])
            order.rotate(n)

        elif op[0] == 'x':
            a, b = (int(x) for x in op[1:].split("/"))
            order[a], order[b] = order[b], order[a]

        else:
            a, b = op[1:].split("/")

            ai = None
            bi = None
            for i, c in enumerate(order):
                if c == a:
                    ai = i
                elif c == b:
                    bi = i

            order[ai], order[bi] = order[bi], order[ai]


    return order


def main():
    ops = input().strip().split(",")
    order = deque([chr(x) for x in range(ord('a'), ord('a') + 16)])

    history = {}
    N = 10 ** 9

    for i in range(1, N + 1):
        order = simulate(order, ops)
        order_frozen = "".join(order)

        if order_frozen in history:
            break

        history[order_frozen] = i


    cycle_l = i - history[order_frozen]

    n = (N - i) % cycle_l

    # 01 23 45 67 89
    # ab ab ab ab ab

    for i in range(n):
        order = simulate(order, ops)

    print("".join(order))




if __name__ == "__main__":
    main()
