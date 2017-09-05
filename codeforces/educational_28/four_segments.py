

INF = 10 ** 9 + 7


def find(cumsums, start, end): # [start, end)
#    import pdb; pdb.set_trace()
    ret = 0
    ret_idx = start

    for i in range(start, end):
        if (cumsums[i] - cumsums[start])  - (cumsums[end-1] - cumsums[i]) > ret:
            ret = (cumsums[i] - cumsums[start]) - (cumsums[end-1] - cumsums[i])
            ret_idx = i

    return (ret, ret_idx)


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]

    cumsums = [0]
    for x in xs:
        cumsums.append(cumsums[-1] + x)

    out = -INF
    idxs = (None, None, None)
    for i in range(n+1):
        f1, idx1 = find(cumsums, 0, i)
        f2, idx2 = find(cumsums, i, n+1)
        if f1 + f2 > out:
            out = f1 + f2
            idxs = (idx1, i, idx2)

    print(*idxs)


if __name__ == "__main__":
    main()

