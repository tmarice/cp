

DIGITS = [
    '0','1','2','3','4','5','6','7','8','9', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def convert(x, r, s):
    m = int(x, r)

    if m == 0:
        return 0

    output = []

    while m:
        output.append(DIGITS[m % s])
        m //= s

    return "".join(output[::-1])


def main():
    n = int(input())

    for _ in range(n):
        x, r, s = input().split()

        r = int(r)
        s = int(s)

        print(convert(x, r, s))

main()
