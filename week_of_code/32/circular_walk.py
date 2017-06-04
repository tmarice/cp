

rs = [-1] * 10000001
def fill_rs(n, g, seed, p):
    for i in range(1, n):
        rs[i] = (rs[i-1] * g + seed) % p


def get_rs(x, n):
    if x < 0:
        while x < 0:
            x += n

    return rs[x % n]


def in_interval(left, right, n, t):
    if left < 0:
        while left < 0:
            left += n

    right %= n

    if left > right:
        return not in_interval(right, left, n, t)
    else:
        if t >= left and t <= right:
            return True
        else:
            return False


def calc(n, s, t):
    stack = [s]
    left = s
    right = s
    i = 0

    import pdb; pdb.set_trace()
    while stack:
        if in_interval(left, right, n, t):
            return i

        new_left = left
        new_right = right
        while stack:
            cur = stack.pop()

            new_left = min(new_left, cur - get_rs(cur, n))
            new_left = min(new_left, cur + get_rs(cur, n) % n)
            new_right = max(new_right, cur + get_rs(cur, n))
            new_right = max(new_right, (cur + get_rs(cur, n) + n) % n)

        j = new_left
        while j != left:
            stack.append(j)
            j += 1

        j = new_right
        while j != right:
            stack.append(j)
            j -= 1

        left = new_left
        right = new_right
        i += 1

    return -1


def main():
    n, s, t = [int(x) for x in raw_input().split()]
    rs[0], g, seed, p = [int(x) for x in raw_input().split()]

    if s == t:
        print 0
    else:
        fill_rs(n, g, seed, p)

        print calc(n, s, t)


main()
