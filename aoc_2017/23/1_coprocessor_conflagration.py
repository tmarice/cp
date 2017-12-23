
import sys
from collections import defaultdict


def simulate(ops):

    def get_val(x):
        if x.islower():
            return registers[x]
        else:
            return int(x)

    registers = defaultdict(int)

    ret = 0
    n = len(ops)
    i = 0
    import pdb; pdb.set_trace()
    while 0 <= i < n:
        cmd, x, y = ops[i].strip().split()

        if cmd == "jnz":
            x = get_val(x)
        y = get_val(y)

        if cmd == "set":
            registers[x] = y
        elif cmd == "sub":
            registers[x] -= y
        elif cmd == "mul":
            registers[x] = get_val(x) * y
            ret += 1
        elif cmd == "jnz":
            if x != 0:
                i += y
                continue

        i += 1

    return ret


def main():
    ops = sys.stdin.readlines()

    mul = simulate(ops)
    print(mul)


if __name__ == "__main__":
    main()
