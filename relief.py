import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader("wayland/hp315.shp")
shapes = sf.shapes()
shape = shapes[0]



def drawAll():
    plt.figure()
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x,y, color="black", linewidth=1)
    plt.show()

def drawN(n):
    plt.figure()
    for x in range(n):
        shape = shapes[x]
        x = [i[0] for i in shape.points[:]]
        y = [i[1] for i in shape.points[:]]
        plt.plot(x,y, color="black", linewidth=1)
    plt.show()

drawN(3)