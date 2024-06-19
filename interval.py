import math

class Interval:
    def __init__(self, _min=math.inf, _max=-math.inf):
        self.min = _min
        self.max = _max

    def contains(self, x):
        return self.min <= x <= self.max

    def surrounds(self, x):
        return self.min < x < self.max

    def clamp(self, x):
        if x < self.min:
            return self.min
        if x > self.max:
            return self.max
        return x

Interval.empty = Interval(math.inf, -math.inf)
Interval.universe = Interval(-math.inf, math.inf)
