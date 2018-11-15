import math

class Point:
    def __init__(self, x, y):  # this is the initializer
        self.x = x  # these are member variables
        self.y = y

    def distance(self, p):  # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

    @staticmethod
    def from_polar(r, theta):  # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)

    def __str__(self):  # specify a str conversion
        return '['+str(self.x)+','+str(self.y)+']'
    
    def __repr__(self):
        return f'Point({self.x},{self.y})'

p = Point(5, 2)  # call the initializer, instantiate the class
print(p.x)  # 5
print(p.y)  # 2

print(type(p))  # Point

polar_point = Point.from_polar(5.0, math.pi/6)
print(polar_point)
polar_point.scale(2)
print(polar_point)