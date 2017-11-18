from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 12)

print("[{0}, {1}]".format(p.x, p.y))
