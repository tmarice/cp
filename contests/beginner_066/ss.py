
def main():
    s = raw_input()

    r = 0
    for i in range(2, len(s), 2):
        if s[:i/2] == s[i/2:i]:
            r = i

    print r


if __name__ == "__main__":
    main()

