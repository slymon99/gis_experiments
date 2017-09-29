import numpy as np

with open("data.txt") as f:
    lines = f.readlines()

pts = []
for line in lines:
    pts.append([float(line[0:9]), float(line[10:20]), float(line[25:32]), float("inf")])

source = pts[0]
pts.remove(source)
known = []
known.append(source)
source[3] = 0


def dist(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return np.sqrt(dx ** 2 + dy ** 2)


# find tentative distances to all points in source
for pt in pts:
    cur_dist = dist(pt, source)
    pt[3]=cur_dist

# find closest point
closest = np.argmin(list(i[3] for i in pts))

