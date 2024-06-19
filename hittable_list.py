from hittable import Hittable, HitRecord
from interval import Interval

class HittableList(Hittable):
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def hit(self, r, ray_t, rec):
        temp_rec = HitRecord()
        hitModel = False
        closest_so_far = ray_t.max

        for obj in self.objects:
            if obj.hit(r, Interval(ray_t.min, closest_so_far), temp_rec):
                hitModel = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.mat = temp_rec.mat
                rec.no_specular = temp_rec.no_specular

        return hitModel
