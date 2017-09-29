import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

with open("data.txt") as f:
    lines = f.readlines()

pts = []
for line in lines:
    pts.append([float(line[0:9]), float(line[10:20]), float(line[25:32])])

xs = [i[0] for i in pts]
ys = [i[1] for i in pts]
zs = [i[2] for i in pts]
cs = array(zs)

colmap = cm.ScalarMappable(cmap=cm.hsv)
colmap.set_array(cs)

fig = plt.figure()
ax = fig.gca(projection='3d')
a = ax.scatter(xs, ys, zs, depthshade=False, c=cm.hsv(cs/max(cs)))


plt.show()
