import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader("wayland/hp315.shp")
shapes = sf.shapes()
shape = shapes[0]

plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y, color="black", linewidth=1)
plt.show()


