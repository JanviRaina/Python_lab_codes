def f1(x, y, z):
    return 4 * x + y + 2 * z - 4


def f2(x, y, z):
    return 3 * x + 5 * y + z - 7


def f3(x, y, z):
    return x + y + 3 * z - 3


def gauss(y0, z0):
    count = 0
    x1 = 1 / 4 * (4 - y0 - 2 * z0)
    y1 = 1 / 5 * (7 - z0 - 3 * x1)
    z1 = 1 / 3 * (3 - x1 - y1)
    if (f1(x1, y1, z1) == 0):
        print(x1)
        print(y1)
        print(z1)
    else:
        y0 = y1
        z0 = z1
        gauss(y0, z0)
    return count


y0 = 0
z0 = 0
gauss(y0, z0)
print(gauss(y0, z0))
