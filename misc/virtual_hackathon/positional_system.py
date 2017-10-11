DIGITS = [
    '0','1','2','3','4','5','6','7','8','9', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def convert(x, s):
    if x == 0:
        return 0

    output = []

    while x:
        output.append(DIGITS[x % s])
        x //= s

    return "".join(output[::-1])

def main():
    t = int(input())

    for _ in range(t):
        s = int(input())

        print(convert(s, 16), convert(s, 11))

main()
