
def get_sum(s):
    result = 0

    end = len(s) // 2
    offset = len(s) // 4

    for i in range(end):
        if s[i] == s[i + offset]:
            result += int(s[i])

    return result


def main():
    s = input()
    s += s

    r = get_sum(s)
    print(r)


if __name__ == "__main__":
    main()
