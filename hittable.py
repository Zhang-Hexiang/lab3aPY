from vec3 import Vec3
from ray import Ray

class HitRecord:
    def __init__(self):
        self.p = Vec3()
        self.normal = Vec3()
        self.mat = None
        self.t = 0.0
        self.front_face = True
        self.no_specular = False

    def setNormal(self, r, outward_normal):
        self.front_face = Vec3.dot(r.directionPos, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable:
    def hit(self, r, ray_t, rec):
        raise NotImplementedError
