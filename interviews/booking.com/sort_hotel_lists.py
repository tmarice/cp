from collections import defaultdict


def process_input(s):
    return s.strip().replace(',', '').replace('.', '').lower().split()


def main():
    keywords = set(process_input(raw_input()))

    m = int(raw_input())
    hotels = defaultdict(int)
    
    for _ in range(m):
        id = int(raw_input())

        description = process_input(raw_input())
        score = [word in keywords for word in description].count(True)

        if score > 0:
            hotels[id] += score

    hotels_list = [(score, id) for id, score in hotels.iteritems()]

    for id, _ in sorted(hotels_list, reverse=True):
        print id,


if __name__ == "__main__":
    main()
