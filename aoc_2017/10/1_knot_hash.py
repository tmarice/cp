
N = 256


def reverse(s, start, end, steps):
    if steps == 0:
        return 

    s[start], s[end] = s[end], s[start]

    reverse(s, (start + 1) % N, (end - 1 + N) % N, steps - 1)


def transform(s, lengths):
    skip = 0
    cur_pos = 0

    for l in lengths:
        reverse(s, cur_pos, (cur_pos + l - 1) % N, l // 2)
        cur_pos = (cur_pos + l + skip) % N
        skip += 1


def main():
    lengths = [int(x) for x in input().split(',')]

    s = list(range(N))
    transform(s, lengths)

    print(s[0] * s[1])


if __name__ == "__main__":
    main()
