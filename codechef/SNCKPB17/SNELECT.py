

def solve(s):
    sneks = sum(1 for c in s if c == 's')
    mongs = len(s) - sneks

    s = ["*"] + list(s) + ["*"]
    for i in range(1, len(s)-1):
        if s[i] == "m":
            if s[i-1] == "s":
                s[i-1] = "*"
                sneks -= 1
            elif s[i+1] == "s":
                s[i+1] = "*"
                sneks -= 1

    if sneks > mongs:
        return "snakes"
    elif sneks < mongs:
        return "mongooses"
    else:
        return "tie"


def main():
    t = int(raw_input())

    for _ in range(t):
        s = raw_input()
        print solve(s)


main()
