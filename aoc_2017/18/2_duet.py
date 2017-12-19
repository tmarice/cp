
import sys
from collections import defaultdict
from collections import deque

def program(instructions, recv_q, snd_q, init_p, snd_counter):

    def get_value(x):
        if x.islower():
            return registers[x]
        else:
            return int(x)

    n = len(instructions)
    registers = defaultdict(int)
    registers["p"] = init_p
    done_instructions = 0

    pointer = 0
    while 0 <= pointer < n:
        ops = instructions[pointer].split()

        if ops[0] == "snd":
            snd_counter[0] += 1
            snd_q.appendleft(get_value(ops[1]))
        elif ops[0] == "set":
            registers[ops[1]] = get_value(ops[2])
        elif ops[0] == "add":
            registers[ops[1]] += get_value(ops[2])
        elif ops[0] == "mul":
            registers[ops[1]] *= get_value(ops[2])
        elif ops[0] == "mod":
            registers[ops[1]] %= get_value(ops[2])
        elif ops[0] == "rcv":
            if len(recv_q) > 0:
                registers[ops[1]] = recv_q.pop()
            else:
                yield done_instructions
                done_instructions = 0
                continue

        elif ops[0] == "jgz":
            if get_value(ops[1]) > 0:
                pointer += get_value(ops[2])
                done_instructions += 1
                continue

        done_instructions += 1
        pointer += 1


def main():
    instructions = [s.strip() for s in sys.stdin.readlines()]

    q0 = deque()
    q1 = deque()

    cnt_0 = [0]
    cnt_1 = [0]
    p0 = program(instructions, q0, q1, 0, cnt_0)
    p1 = program(instructions, q1, q0, 1, cnt_1)
    while True:
        try:
            new_0 = next(p0)
        except StopIteration:
            new_0 = 0

        try:
            new_1 = next(p1)
        except StopIteration:
            new_1 = 0

        if new_0 == 0 and new_1 == 0:
            break
        print(new_0, new_1)

    print(cnt_1[0])


if __name__ == "__main__":
    main()
