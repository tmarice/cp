def main():
    n, q = [int(x) for x in raw_input().split()]

    seq_list = [[] for _ in range(n)]
    last_ans = 0

    for _ in range(q):
        t, x, y = [int(x) for x in raw_input().split()]

        if t == 1:
            seq_list[(x^last_ans) % n].append(y)
        else:
            seq = seq_list[(x^last_ans) % n]
            last_ans = seq[y % len(seq)]
            print last_ans


if __name__ == "__main__":
    main()
