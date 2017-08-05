
from collections import defaultdict


def main():
    s = raw_input()
    k = int(raw_input())

    count = defaultdict(list)

    for i, c in enumerate(s):
        count[c].append(i)

    candidates = [(c, n) for c, n in count.iteritems() if len(n) >= k]
    output = []

    i = -1
    for c, index_list in sorted(candidates, reverse=True):
        if i == len(s):
            break
        
        cand_out = []
        tmp_i = i

        for ind in index_list:
            if ind > tmp_i:
                tmp_i = ind
                cand_out.append(c)

        if len(cand_out) >= k:
            output.extend(cand_out)
            i = tmp_i

    print "".join(output)


if __name__ == "__main__":
    main()
