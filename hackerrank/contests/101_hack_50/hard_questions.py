
def main():
    n = int(raw_input())
    vincent = raw_input()
    catherine = raw_input()

    res = 0
    for i in range(n):
        if vincent[i] != '.':
            if vincent[i] != catherine[i]:
                res += 1

    print res


if __name__ == "__main__":
    main()
