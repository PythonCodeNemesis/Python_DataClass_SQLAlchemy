from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int
    z: int = field(default=0)

p = Point(1, 2)
p.x = 3
p.y = 4

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2) # True

p3 = Point(1,2,3)
p4 = dataclasses.replace(p3,z=4)