

def can_finish(hs, e):
    for h in hs:
        if h > e:
            e -= h - e
        else:
            e += e - h

        if e < 0:
            return False

    return True


def bs(hs, start, end):
    if start > end:
        return None
    elif start == end:
        return start

    mid = start + (end - start) / 2

    if can_finish(hs, mid):
        return bs(hs, start, mid)
    else:
        return bs(hs, mid+1, end)



n = int(raw_input())
hs = [int(x) for x in raw_input().split()]


print bs(hs, 0, 10 ** 5)
