
from collections import defaultdict
import operator
import sys


COND_MAP = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}

OP_MAP = {
    "inc": operator.add,
    "dec": operator.sub,
}


def main():
    regs = defaultdict(int)
    result = 0

    for line in sys.stdin:
        reg, op, x, _, cond_1, cond_2, cond_3 = line.split()

        if COND_MAP[cond_2](regs[cond_1], int(cond_3)):
            regs[reg] = OP_MAP[op](regs[reg], int(x))

            if regs[reg] > result:
                result = regs[reg]

    print(result)


if __name__ == "__main__":
    main()
