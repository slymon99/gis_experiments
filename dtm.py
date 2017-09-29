import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import os

pts = []

for filename in os.listdir("dtm"):
    if filename.endswith(".dtm"):
        print("parsing " + filename)
        with open("dtm/" + filename) as f:
            lines = f.readlines()

        # append points to pts: handles inconsistant data format


        if (lines[0][0:1] == " "):
            for x in range(len(lines) - 1):
                line = lines[x]
                pts.append([float(line[1:10]), float(line[11:21]), float(line[26:33])])
        else:
            for x in range(len(lines) - 1):
                line = lines[x]

                pts.append([float(line[0:9]), float(line[10:20]), float(line[25:32])])

print(len(pts))
xs = array([i[0] for i in pts])
ys = array([i[1] for i in pts])
zs = array([i[2] for i in pts])
print(str(max(zs)) + " " + str(min(zs)))

colmap = cm.ScalarMappable(cmap=cm.hsv)
colmap.set_array(zs)


def three():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_zlim(200, 700)
    ax.scatter(xs, ys, zs, depthshade=False, c=cm.hsv(zs / max(zs)))
    plt.show()


def two():
    plt.scatter(xs, ys, marker="s", s=1, c=cm.hsv(zs / max(zs)))
    plt.show()


two()
