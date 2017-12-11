
def get_sum(s):
    result = 0

    end = len(s) - 1
    for i in range(end):
        if s[i] == s[i + 1]:
            result += int(s[i])

    return result


def main():
    s = input()
    s += s[0]

    r = get_sum(s)
    print(r)


if __name__ == "__main__":
    main()
