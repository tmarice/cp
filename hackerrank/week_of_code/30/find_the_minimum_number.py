

def get_min_string(x):
    if x == 2:
        return "min(int, int)"
    else:
        return "min(int, {0})".format(get_min_string(x-1))


n = int(raw_input())

s = get_min_string(n)

print s
