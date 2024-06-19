import math

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.e = [x, y, z]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, val):
        self.e[i] = val

    def __iadd__(self, other):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t):
        return self.__imul__(1 / t)

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2

    def near_zero(self):
        s = 1e-8
        return abs(self.e[0]) < s and abs(self.e[1]) < s and abs(self.e[2]) < s

    def __add__(self, other):
        return Vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])

    def __sub__(self, other):
        return Vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.e[0] * t.e[0], self.e[1] * t.e[1], self.e[2] * t.e[2])
        else:
            return Vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)

    def __rmul__(self, t):
        return self.__mul__(t)

    def __truediv__(self, t):
        return self.__mul__(1 / t)

    @staticmethod
    def dot(u, v):
        return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]

    @staticmethod
    def cross(u, v):
        return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1], u.e[2] * v.e[0] - u.e[0] * v.e[2], u.e[0] * v.e[1] - u.e[1] * v.e[0])

    @staticmethod
    def unit_vector(v):
        return v / v.length()

    @staticmethod
    def reflect(v, n):
        return v - 2 * Vec3.dot(v, n) * n

    def __repr__(self):
        return f"Vec3({self.e[0]}, {self.e[1]}, {self.e[2]})"
