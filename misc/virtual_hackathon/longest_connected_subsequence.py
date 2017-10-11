
import fileinput



def solve(k, seq):
    max_len = 0

    n = len(seq)
    i = 0
    j = 0
    cur_count = 0

    while i < n and j < n:
        if seq[i] == '1':
            cur_count  += 1

        while cur_count > k:
            if seq[j] == '1':
                cur_count -= 1
            j += 1

        max_len = max(max_len, i - j + 1)
        i += 1

    max_len = max(max_len, i - j + 1)

    return max_len


def main():
    for i, line in enumerate(fileinput.input()):
        if i % 2 == 0:
            k = int(line)
        else:
            print(solve(k, line.strip()))


if __name__ == "__main__":
    main()
