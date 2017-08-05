

def calc_set():
    s = range(1, 501)
    s[2] = -1


    for i in range(2, 500):
        if s[i] == -1:
            continue
        else:
            for j in range(i):
                if s[i] != -1 and s[j] != -1 and s[i] + s[j] < 501:
                    s[s[i]+s[j]-1] = -1

    return [x for x in s if x != -1]

def main():
    s = calc_set()

    t = int(raw_input())

    for _ in range(t):
        n = int(raw_input())

        for i in range(n):
            print s[i],
        print


main()
