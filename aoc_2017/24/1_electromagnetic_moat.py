
import sys


def get_strongest(elements):

    def explore(port, strength, used):
        ret = 0

        last = True
        for cn in (e for e in elements if e not in used):
            if cn[0] == port or cn[1] == port:
                other = cn[0] if port == cn[1] else cn[1]
                last = False

                used.add(cn)
                ret = max(ret, explore(other, strength + cn[0] + cn[1], used))
                used.remove(cn)

        if last:
            return strength
        else:
            return ret

    return explore(0, 0, set())


def main():
    elements = []
    for line in sys.stdin:
        elements.append(tuple(int(x) for x in line.strip().split("/")))

    s = get_strongest(elements)
    print(s)


if __name__ == "__main__":
    main()
