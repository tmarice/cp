
from functools import reduce
from operator import xor


N = 256


def get_dense_hash(s):
    return [reduce(xor, s[i * 16: i * 16 + 16])
            for i in range(16)]


def reverse(s, start, end, steps):
    if steps == 0:
        return

    s[start], s[end] = s[end], s[start]

    reverse(s, (start + 1) % N, (end - 1 + N) % N, steps - 1)


def knot_hash(s):
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    s = list(range(N))
    skip = 0
    cur_pos = 0

    for _ in range(64):
        for l in lengths:
            reverse(s, cur_pos, (cur_pos + l - 1) % N, l // 2)
            cur_pos = (cur_pos + l + skip) % N
            skip += 1

    dh = get_dense_hash(s)
    kh = ''.join("{0:02x}".format(h) for h in dh)

    return kh


def count_set(s):
    return sum(int(c) for c in "{0:b}".format(int(s, 16)))


def solve(s):
    total_set = 0

    for i in range(128):
        kh = knot_hash("{0}-{1}".format(s, i))
        total_set += count_set(kh)

    return total_set


def main():
    s = input().strip()

    d = solve(s)

    print(d)



if __name__ == "__main__":
    main()
