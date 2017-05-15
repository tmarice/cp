

def invert(s):
    ret = ["1" if c == "0" else "0" for c in s]

    return "".join(ret)


def main():
    s = "0"

    import pdb; pdb.set_trace()
    while len(s) < 1000:
        t = invert(s)
        s = s + t

    q = int(raw_input())
    for _ in range(q):
        x = int(raw_input())

        print s[x]


main()
