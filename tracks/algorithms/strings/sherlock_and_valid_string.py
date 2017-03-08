
from collections import defaultdict


def calculate(s):
    for c in s:
        letters[c] += 1

    letter_counts = defaultdict(int)

    for l, c in letters.iteritems():
        letter_counts[c] += 1

    if len(letter_counts) == 1:
        return "YES"
    elif len(letter_counts) == 2:
        x = letter_counts.items() # [(count_1, sum_1), (count_2, sum_2)]

        if x[0][1] == 1:
            if x[0][0] == 1 or x[0][0] == x[1][0] + 1:
                return "YES"
        elif x[1][1] == 1:
            if x[1][0] == 1 or x[1][0] == x[0][0] + 1:
                return "YES"

    return "NO"


letters = defaultdict(int)
s = raw_input()

print calculate(s)

