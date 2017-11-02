

numbers = set("0123456789")
lower_case = set("abcdefghijklmnopqrstuvwxyz")
upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = set("!@#$%^&*()-+")


def count_req(s):
    num = 1
    lc = 1
    uc = 1
    sc = 1

    if any(c in numbers for c in s):
        num = 0

    if any(c in lower_case for c in s):
        lc = 0

    if any(c in upper_case for c in s):
        uc = 0

    if any(c in special_characters for c in s):
        sc = 0

    return num + lc + uc + sc


def main():
    n = int(input())
    s = input()

    extra = count_req(s)
    length = max(0, 6 - n)

    print(max(length, extra))


if __name__ == "__main__":
    main()
