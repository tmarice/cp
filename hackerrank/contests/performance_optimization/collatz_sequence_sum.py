
from collections import deque
from collections import defaultdict

nx = [0, 1, 2, 3, 3, 3, 6, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 18, 18, 18, 18, 18, 18, 18, 25, 25, 25, 25, 25, 25, 25, 25, 33, 33, 33, 33, 33, 33, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 105, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 169, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 219, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 295, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 379, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 505, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 673, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 897, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 1794, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 3588, 0]

def collatzSequenceSum(T, A, B):
    """
    memo = {}
    q = deque([(1, 1)])

    while q:
        cur_x, cur_len = q.pop()

        if cur_x not in memo:
            memo[cur_x] = cur_len
        else:
            continue

        if cur_x * 2 < 5003:
            q.appendleft((cur_x * 2, cur_len + 1))

        if (cur_x - 1) % 3 == 0 and ((cur_x - 1) / 3) % 2 == 1:
            q.appendleft(((cur_x - 1) / 3, cur_len + 1))

    #import pdb; pdb.set_trace()
    nx = [0] * 5004

    longest = 1
    gk = 1

    nx[1] = 1

    for i in range(2, 5003):
        if memo.get(i, 0) > longest:
            longest = memo.get(i, 0)
            gk = i

        nx[i] = gk
"""

    s = 0
    n = 0

    for i in range(T):
        n = (A * n + B) % 5003
        s += nx[n]

    return s


def main():
    t, a, b = (int(x) for x in input().split())

    print(collatzSequenceSum(t, a, b))


main()


