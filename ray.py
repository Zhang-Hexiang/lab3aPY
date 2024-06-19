from vec3 import Vec3

class Ray:
    def __init__(self, origin, direction):
        self.originPos = origin
        self.directionPos = direction

    def hitPos(self, t):
        return self.originPos + t * self.directionPos
