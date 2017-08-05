def get_distance(rq, cq, r, c):
    if rq == r:
        return abs(c - cq)
    elif cq == c:
        return abs(r - rq)
    elif abs(rq - r) == abs(cq - c):
        return abs(rq - r)
    else:
        return -1


def get_direction(rq, cq, r, c):
    """ Return in which direction lies (r,c) as opposed to (rq, cq) """

    if rq == r and cq < c:
        return "R"
    elif rq == r and cq > c:
        return "L"
    elif cq == c and rq < r:
        return "U"
    elif cq == c and rq > r:
        return "D"
    elif rq - r > 0 and cq - c > 0:
        return "DL"
    elif rq - r > 0 and cq - c < 0:
        return "DR"
    elif rq - r < 0 and cq - c > 0:
        return "UL"
    elif rq - r < 0 and cq - c < 0:
        return "UR"


def get_max_dist(rq, cq, n, d):
    if d == "R":
        return n - cq
    elif d == "L":
        return cq - 1
    elif d == "U":
        return n - rq
    elif d == "D":
        return rq - 1
    elif d == "UL":
        return min(cq - 1, n - rq)
    elif d == "UR":
        return min(n - rq, n - cq)
    elif d == "DL":
        return min(rq - 1, cq - 1)
    elif d == "DR":
        return min(rq - 1, n - cq)


DIRECTIONS = ["U", "D", "L", "R", "UR", "UL", "DR", "DL"]


def get_count(n, rq, cq, obstacles):
    dist = {d:get_max_dist(rq, cq, n, d) for d in DIRECTIONS}

    for k in obstacles:
        d = get_direction(rq, cq, *k)
        obstacle_dist = get_distance(rq, cq, *k)

        if obstacle_dist != -1:
            dist[d] = min(dist[d], obstacle_dist - 1)

    return sum(dist.itervalues())


def main():
    n, k = [int(x) for x in raw_input().split()]
    rq, cq = [int(x) for x in raw_input().split()]

    obstacles = []
    for _ in range(k):
        r, c = [int(x) for x in raw_input().split()]
        obstacles.append((r, c))

    print get_count(n, rq, cq, obstacles)


if __name__ == "__main__":
    main()
