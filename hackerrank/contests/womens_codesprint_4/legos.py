



def main():
    t = int(input())

    for _ in range(t):
        s = [int(x) for x in input().split()]
        a, b = (int(x) for x in input().split())

        s.remove(a)
        s.remove(b)

        t = 1
        for x in s:
            t *= x

        print(t)


if __name__ == "__main__":
    main()
