from math import sqrt, cos, sin
class Point:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z 
    def __getitem__(self, index):
        return self[index]
    def __eq__(self, other):
        return (epsilonEq(self.x, other.x)) & (epsilonEq(self.y, other.y)) & (epsilonEq(self.z, other.z))
    def __str__(self):
        return f"{self.x} {self.y} {self.z}"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    def uniRound(self, roundDecimal = 6):
        round(self.x, roundDecimal)
        round(self.y, roundDecimal)
        round(self.z, roundDecimal)
    def transfromToList(self):
        return [self.x, self.y, self.z]
    def pointToDistance(self):
        return sqrt(self.x**2 + self.y**2 + self.z ** 2)
    def distanceToPoint(self, a):
        if not isinstance(a, Point):
            raise TypeError("a must be a Point")
        return sqrt((self.x-a.x)**2 + (self.y-a.y)**2 + (self.z-a.z)**2)
    def distance2D(self, a):
        if not isinstance(a, Point):
            raise TypeError("a must be a Point")
        return sqrt((self.x-a.x)**2 + (self.y - a.y)**2)
    def rotateXY(self, angle):
        return Point(self.x * cos(angle) - self.y * sin(angle), self.x * sin(angle) + self.y * cos(angle), self.z)
    def translateTo(self, a, angle = 0): #we're translating this point to a
        if not isinstance(a, Point):
            raise TypeError("a must be a Point")
        self.x = self.x - a.x
        self.y = self.y - a.y
        self.z = self.z - a.z
EPSILON = 0.000001
def epsilonEq(a, b):
    if (a < b) & ((a + EPSILON) < b):
        return 0
    if (a > b) & ((a - EPSILON) > b):
        return 0
    return 1
