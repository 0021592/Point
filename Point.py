from math import sqrt, cos, sin
class Point(BaseException):
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        if isinstance(x, list) or isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z 
    def __copy__(self):
        return Point(self.x, self.y, self.z)
    def __deepcopy__(self, memo): #x, y, z are numbers, so this is a full copy, and much faster than the generic one (Point is a BaseException)
        return Point(self.x, self.y, self.z)
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")
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
    def transformToList(self):
        return [self.x, self.y, self.z]
    def distanceToOrigin(self):
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
def epsilonEq(a, b, EPSILON = EPSILON):
    if (a < b) & ((a + EPSILON) < b):
        return 0
    if (a > b) & ((a - EPSILON) > b):
        return 0
    return 1
