

def main():
    n, m = (int(x) for x in input().split())
    n += 1
    m += 1

    print(n * m - 2 * (n + m) + 4)


if __name__ == "__main__":
    main()
