

def valid(s):
    s_count = 0
    for c in s:
        if c == "H":
            s_count += 1
        elif c == "T":
            s_count -= 1

        if s_count != 0 and s_count != 1:
            return False

    if s_count == 0:
        return True
    else:
        return False


def main():
    r = int(raw_input())

    for _ in range(r):
        l = int(raw_input())
        s = raw_input()

        print "Valid" if valid(s) else "Invalid"

if __name__ == "__main__":
    main()
