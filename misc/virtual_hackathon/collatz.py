

def calc(x):
    step = 0

    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x + 1

        step += 1

    return step


def main():
    t = int(input())

    for _ in range(t):
        print(calc(int(input())))

main()
