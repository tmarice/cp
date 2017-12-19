
import sys
from collections import defaultdict


def main():

    def get_value(x):
        if x.islower():
            return registers[x]
        else:
            return int(x)

    instructions = [s.strip() for s in sys.stdin.readlines()]

    n = len(instructions)
    registers = defaultdict(int)
    last_sound = None

    pointer = 0
    while 0 <= pointer < n:
        ops = instructions[pointer].split()

        if ops[0] == "snd":
            last_sound = get_value(ops[1])
        elif ops[0] == "set":
            registers[ops[1]] = get_value(ops[2])
        elif ops[0] == "add":
            registers[ops[1]] += get_value(ops[2])
        elif ops[0] == "mul":
            registers[ops[1]] *= get_value(ops[2])
        elif ops[0] == "mod":
            registers[ops[1]] %= get_value(ops[2])
        elif ops[0] == "rcv":
            if registers[ops[1]] != 0:
                break
        elif ops[0] == "jgz":
            if get_value(ops[1]) > 0:
                pointer += get_value(ops[2])
                continue

        pointer += 1

    print(last_sound)


if __name__ == "__main__":
    main()
