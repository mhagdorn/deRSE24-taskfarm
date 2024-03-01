from matplotlib import pyplot
import pandas
import numpy
from numpy import random


def gen_points_uniform(xsize, ysize, npoints):
    x = random.uniform(high=xsize, size=npoints)
    y = random.uniform(high=ysize, size=npoints)
    return numpy.column_stack((x, y))


def gen_points_path(xsize, ysize, npoints, dist=50, slope=2):
    npath = int(xsize//(2*dist))
    ny = int(npoints//npath)
    npoints = ny*npath
    pnts = numpy.zeros((npoints, 2), dtype=float)
    for i in range(npath):
        s = i*ny
        e = (i+1)*ny
        y = numpy.linspace(0, ysize, ny)
        x = dist + 2*i*dist + y/2 + random.normal(scale=dist/2, size=ny)
        x = numpy.where(x > xsize, x-xsize, x)
        x = numpy.where(x < 0, x+xsize, x)
        pnts[s:e, 0] = x
        pnts[s:e, 1] = y

    return pnts


def main():
    XSIZE = 300
    YSIZE = 200
    GSIZE = 50
    NPNTS = 1000

    pnts = gen_points_path(XSIZE, YSIZE, NPNTS)
    data = pandas.DataFrame({"x": pnts[:, 0], "y": pnts[:, 1]})

    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # the points
    ax.plot(data["x"], data["y"], '.')
    pyplot.savefig("problem_1.pdf")

    # the grid
    for x in range(0, XSIZE+GSIZE, GSIZE):
        ax.axvline(x)
    for y in range(0, YSIZE+GSIZE, GSIZE):
        ax.axhline(y)
    pyplot.savefig("problem_2.pdf")

    # the post
    p = numpy.array((1.5, 1.5)) * GSIZE
    ax.plot(p[0], p[1], "ro")
    pyplot.savefig("problem_3.pdf")

    # circle interesting points
    radius = .75*GSIZE
    circle = pyplot.Circle(p, radius, color='r', fill=False)
    ax.add_patch(circle)
    pyplot.savefig("problem_4.pdf")

    # the square
    rectangle = pyplot.Rectangle(
        p-numpy.array([radius, radius]),
        2*radius, 2*radius, color="k", fill=False)
    ax.add_patch(rectangle)
    pyplot.savefig("problem_5.pdf")

    # ignore points outside the box
    data["x_trans"] = data["x"] - p[0]
    data["y_trans"] = data["y"] - p[1]
    data["outside"] = numpy.logical_or(
        numpy.abs(data["x_trans"]) > radius,
        numpy.abs(data["y_trans"]) > radius)
    ax.plot(data[data["outside"]]["x"], data[data["outside"]]["y"], 'k.')
    pyplot.savefig("problem_6.pdf")

    # points inside circle
    data["distance"] = numpy.sqrt(
        data["x_trans"] * data["x_trans"] +
        data["y_trans"] * data["y_trans"])
    data["outside2"] = data["distance"] >= radius
    ax.plot(data[data["outside2"]]["x"], data[data["outside2"]]["y"], 'k.')
    pyplot.savefig("problem_7.pdf")

    #pyplot.show()


if __name__ == '__main__':
    main()
