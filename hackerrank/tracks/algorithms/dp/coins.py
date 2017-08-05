

memo = {}

def calc(total, first_c):
    if total < 0:
        return 0

    if first_c < 0:
        return 0

    if total == 0:
        return 1

    if (total, first_c) in memo:
        return memo[(total, first_c)]

    ret = calc(total-cs[first_c], first_c) + calc(total, first_c-1)

    memo[(total, first_c)] = ret
    return ret


n, m = [int(x) for x in raw_input().split()]
cs = [int(x) for x in raw_input().split()]

out = calc(n, m-1)
print out

