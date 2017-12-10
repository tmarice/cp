
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


def transform(s, lengths):
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


def main():
    lengths = [ord(x) for x in input().strip()] + [17, 31, 73, 47, 23]

    s = list(range(N))
    kh = transform(s, lengths)

    print(kh)


if __name__ == "__main__":
    main()
