


def main():
    r, g, b = [int(x) for x in raw_input().split()]

    if (g * 10 + b) % 4 == 0:
        print "YES"
    else:
        print "NO"

main()
