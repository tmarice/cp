
def main():
    swipes = [int(x) for x in raw_input().split()]

    out = 0
    for s in swipes:
        out += min(s, 10) * 10

    print out


if __name__ == "__main__":
    main()
