

def main():
    l = [int(x) for x in raw_input().split()]

    print l[0],

    for i in range(1, len(l)):
        diff = l[i] - l[i-1]

        if -127 <= diff <= 127:
            print diff,
        else:
            print -128, diff,


if __name__ == "__main__":
    main()
