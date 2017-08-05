
from collections import defaultdict

def main():
    n = int(raw_input())

    hotels = defaultdict(list)

    for _ in range(n):
        hotel_id, rating = [int(x) for x in raw_input().split()]
        hotels[hotel_id].append(rating)

    ratings = [(-sum(rs) / float(len(rs)), h_id) for h_id, rs in hotels.iteritems()]
    import pdb; pdb.set_trace()

    for _, hotel_id in sorted(ratings):
        print hotel_id


if __name__ == "__main__":
    main()
