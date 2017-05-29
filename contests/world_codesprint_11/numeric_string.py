

def magic(s, k, b, m):
    msb = b ** (k-1) % m
    n = len(s)

    magic_sum = 0
    cur_sum = 0
    for i in xrange(k):
        cur_sum = (cur_sum * b + int(s[i])) % m

    for i in xrange(k, n):
        magic_sum += cur_sum % m
        cur_sum = (((cur_sum - (int(s[i-k]) * msb) % m) * b) % m + int(s[i])) % m

    return magic_sum + cur_sum % m


def main():
    s = raw_input()
    k, b, m = [int(x) for x in raw_input().split()]

    print magic(s, k, b, m)


main()
