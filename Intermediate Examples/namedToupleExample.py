import collections
from collections import namedtuple 

Point = namedtuple('Point', 'x y x')

newP = Point(3, 4, 5)

print(newP.x, newP.y, newP.z)
print(newP._fields)