
from collections import namedtuple
from math import radians, acos, sin, cos
from operator import attrgetter
from itertools import chain

Destination = namedtuple("Destination", ("name", "latitude", "longitude", "passions"))
INF = 1000000000

EARTH_RADIUS = 6371

def dist(point1, point2):
    point1_lat_in_radians  = radians( point1.latitude )
    point2_lat_in_radians  = radians( point2.latitude )
    point1_long_in_radians = radians( point1.longitude )
    point2_long_in_radians = radians( point2.longitude )

    return acos( sin( point1_lat_in_radians ) * sin( point2_lat_in_radians ) +
                 cos( point1_lat_in_radians ) * cos( point2_lat_in_radians ) *
                 cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS


n = int(raw_input())

group_passions = set([])
for _ in range(n):
    l = raw_input().split()

    group_passions.update(l[1:])

destinations = []
y = int(raw_input())
for _ in range(y):
    l = raw_input().split()
    destinations.append(Destination(l[0], float(l[1]), float(l[2]), set(l[4:])))

max_passions = 0
candidates = []

for i in range(len(destinations)-1):
    for j in range(i+1, len(destinations)):
        dest_passions = destinations[i].passions | destinations[j].passions
        common = len(dest_passions & group_passions)
        if common > max_passions:
            max_passions = common
            candidates = []
        if common == max_passions:
            candidates.append((dist(destinations[i], destinations[j]), destinations[i], destinations[j]))


import pdb; pdb.set_trace()
out = min(candidates)

print min(out[1].name, out[2].name), max(out[1].name, out[2].name)
