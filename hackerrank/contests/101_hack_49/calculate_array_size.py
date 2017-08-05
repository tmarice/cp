
from math import floor


def main():
    n = int(raw_input())
    ds = [int(x) for x in raw_input().split()]

    r = 4
    for d in ds:
        r *= d

    print int(floor(r / 1024.))



