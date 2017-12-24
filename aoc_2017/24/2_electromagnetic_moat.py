
import sys


def get_strongest(elements):

    def explore(port, strength, used):
        ret_length = 0
        ret_strength = 0

        last = True
        for cn in (e for e in elements if e not in used):
            if cn[0] == port or cn[1] == port:
                other = cn[0] if port == cn[1] else cn[1]
                last = False

                used.add(cn)
                nl, ns = explore(other, strength + cn[0] + cn[1], used)
                if nl > ret_length:
                    ret_length = nl
                    ret_strength = ns
                elif nl == ret_length:
                    ret_strength = max(ret_strength, ns)
                used.remove(cn)

        if last:
            return len(used), strength
        else:
            return ret_length, ret_strength

    return explore(0, 0, set())


def main():
    elements = []
    for line in sys.stdin:
        elements.append(tuple(int(x) for x in line.strip().split("/")))

    l, s = get_strongest(elements)
    print(l, s)


if __name__ == "__main__":
    main()
