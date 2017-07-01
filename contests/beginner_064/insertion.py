
def main():
    n = int(raw_input())
    s = raw_input()

    total = 0
    prep = 0
    for c in s:
        if c == '(':
            total += 1
        else:
            total -= 1

        if total < 0:
            prep += 1
            total = 0

    print '(' * prep + s + ')' * total


main()


