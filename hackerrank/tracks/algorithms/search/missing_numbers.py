

def get_freq(x):
    ret = [0] * 10001

    for c in x:
        ret[c] += 1

    return ret


n = int(raw_input())
a = [int(x) for x in raw_input().split()]

m = int(raw_input())
b = [int(x) for x in raw_input().split()]

freq_a = get_freq(a)
freq_b = get_freq(b)

for i in range(10001):
    if freq_a[i] < freq_b[i]:
        print i,
