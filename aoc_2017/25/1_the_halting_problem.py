
import sys
from collections import defaultdict


DIRECTIONS = {
    "right": 1,
    "left": -1,
}


def simulate(start_state, checksum, instructions):
    tape = defaultdict(int)

    state = start_state
    position = 0
    for _ in range(checksum):
        value = tape[position]
        new_value, step, state = instructions[state][value]

        tape[position] = new_value
        position += step

    return sum(tape.values())


def main():
    instructions = defaultdict(dict)

    lines = sys.stdin.readlines()

    start_state = lines[0].strip().split()[-1][:-1]
    checksum = int(lines[1].strip().split()[-2])

    i = 3
    while i < len(lines):
        state = lines[i].strip().split()[-1][:-1]

        for _ in range(2):
            value = int(lines[i + 1].strip().split()[-1][:-1])
            new_value = int(lines[i + 2].strip().split()[-1][:-1])
            move = DIRECTIONS[lines[i + 3].strip().split()[-1][:-1]]
            new_state = lines[i + 4].strip().split()[-1][:-1]

            instructions[state][value] = (new_value, move, new_state)

            i += 4
        i += 2

    import pdb; pdb.set_trace()
    r = simulate(start_state, checksum, instructions)
    print(r)


if __name__ == "__main__":
    main()
