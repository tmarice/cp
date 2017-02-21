
def exchange(strings, a, b):
    strings[a], strings[b] = strings[b], strings[a]


def compare(a, b):
    i = 0
    j = 0

    while a[i] == a[j] and i < len(a) and j < len(b):
        i += 1
        j += 1

    





def three_way_qs(strings, lo, hi, k):
    if hi <= lo:
        return

    lt = lo
    gt = hi
    i = lo + 1

    v = char_at(strings[lo], k)

    while i <= gt:
        t = char_at(strings[i], k)

        if t < v:
            exchange(strings, i, lt)
            i += 1
            lt += 1
        elif t > v:
            exchange(strings, i, gt)
            gt -= 1
        else:
            i += 1

    three_way_qs(strings, lo, lt-1, k)

    if v >= 0:
        three_way_qs(strings, lt, gt, k+1)

    three_way_qs(strings, gt+1, hi, k)


n = int(raw_input())
strings = []

for _ in range(n):
    strings.append(raw_input().strip())

three_way_qs(strings, 0, n-1, 0)

for s in strings:
    print s
