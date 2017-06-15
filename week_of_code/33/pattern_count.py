


def count(s):
    out = 0
    state = 0

    for c in s:
        if state == 0:
            if c == '1':
                state = 1
        elif state == 1:
            if c == '0':
                state = 2
            elif c == '1':
                state = 1
            else:
                state = 0
        elif state == 2:
            if c == '0':
                pass
            elif c == '1':
                state = 1
                out += 1
            else:
                state = 0

    return out



def main():
    q = int(raw_input())

    for _ in range(q):
        s = raw_input()
        print count(s)


main()
