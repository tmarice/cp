

def get_combinations(xs, i):
    if i == len(xs):
        return [""]
    
    ret = []
    for comb in get_combinations(xs, i+1):
        ret.append(comb)
        ret.append(xs[i] + comb)

    return ret


def find_all_possible_teams():
    xs = sorted(raw_input())

    combinations = get_combinations(xs, 0)

    for comb in sorted(combinations, key=lambda x: (len(x), x)):
        if comb:
            print comb


find_all_possible_teams()
