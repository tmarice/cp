
def main():
    n = int(input())
    ss = []

    for _ in range(n):
        ss.append(input().split())

    key, rev, cp = input().split()

    key = int(key) - 1
    rev = True if rev == "true" else False
    numeric = True if cp == "numeric" else False

    ss.sort(key = lambda x: int(x[key]) if numeric else x[key])

    it = reversed(ss) if rev else ss

    for s in it:
        for subs in s:
            print(subs, end=" ")
        print()


if __name__ == "__main__":
    main()
