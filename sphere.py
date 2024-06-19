from hittable import Hittable, HitRecord
from vec3 import Vec3
from interval import Interval
from ray import Ray
import math

class Sphere(Hittable):
    def __init__(self, center, radius, material, no_specular=False):
        self.center = center
        self.radius = radius
        self.mat = material
        self.no_specular = no_specular

    def hit(self, r, ray_t, rec):
        lightToCenter = r.originPos - self.center
        a = Vec3.dot(r.directionPos, r.directionPos)
        half_b = Vec3.dot(lightToCenter, r.directionPos)
        c = Vec3.dot(lightToCenter, lightToCenter) - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False
        sqrtd = math.sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        if not ray_t.surrounds(root):
            root = (-half_b + sqrtd) / a
            if not ray_t.surrounds(root):
                return False

        rec.t = root
        rec.p = r.hitPos(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.setNormal(r, outward_normal)
        rec.mat = self.mat  # Ensure material is set
        rec.no_specular = self.no_specular

        return True
