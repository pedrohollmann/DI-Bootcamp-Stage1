import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return f"Circle(radius={self._radius})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius + other._radius)
        return NotImplemented

    def __gt__(self, other):
        return self._radius > other._radius

    def __eq__(self, other):
        return self._radius == other._radius

    def __lt__(self, other):
        return self._radius < other._radius


c1 = Circle(3)
c2 = Circle(5)
c3 = Circle(2)
c4 = Circle(4)

print(c1)
print(c1.radius)
print(c1.diameter)

print(c1.area())

c5 = c1 + c2
print(c5)

print(c2 > c1)
print(c3 == c4)

circles = [c1, c2, c3, c4]
circles.sort()

print(circles)