
m, w, p, n = [int(x) for x in raw_input().split()]

i = 0
cur_candy = 0
min_i = 1000000000

while True:
    i += 1
    cur_candy += m * w

    rest = i + max(n - cur_candy, 0) / (m + w)
    if rest < min_i:
        min_i = rest

    if cur_candy >= n:
        break

    if cur_candy >= p:
        add = cur_candy / p

        if m < w:
            d = w - m
            c = min(d, add)
            m += c
            add -= c
            cur_candy -= c * p
        elif w < m:
            d = m - w
            c = min(d, add)
            w += c
            cur_candy -= c * p
            add -= c

        if add:
            half = add / 2

            m += half
            w += add - half

            cur_candy -= add * p

print min_i



