
def get_weights(s):
    ret = set()

    i = 0
    while i < len(s):
        count = 0
        current_char = s[i]

        while i < len(s) and s[i] == current_char:
            count += 1
            i += 1

        weight = ord(current_char) - ord('a') + 1
        for j in range(1, count+1):
            ret.add(weight * j)

    return ret


def main():
    s = raw_input()
    n = int(raw_input())
    queries = []

    for _ in range(n):
        queries.append(int(raw_input()))

    weights = get_weights(s)

    for x in queries:
        if x in weights:
            print "Yes"
        else:
            print "No"


if __name__ == "__main__":
    main()

