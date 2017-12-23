
from math import sqrt

def prime(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False

    return True


def main():
    b = 93300
    c = 110300
    h = 0

    for b in range(106700,  123700+1, 17):
        if not prime(b):
            h += 1

    print(h)


if __name__ == "__main__":
    main()
