import random
from vec3 import Vec3
from ray import Ray
from color import write_color
from hittable import HitRecord
from interval import Interval
from light import PointLight, ParallelLight
from image_data import ImageData
from PIL import Image

class Camera:
    def __init__(self):
        self.center = Vec3(0, 0, 0)
        self.image_width = 100
        self.image_height = 100
        self.samples_per_pixel = 10
        self.max_depth = 10
        self.background_color = Vec3(0, 0, 0)
        self.output = "output.png"

    def render(self, world, lights):
        self.initialize()
        data = ImageData(self.image_height, self.image_width)

        for j in range(self.image_height):
            for i in range(self.image_width):
                pixel_color = Vec3(0, 0, 0)
                for sample in range(self.samples_per_pixel):
                    r = self.get_ray(i, j)
                    pixel_color += self.ray_color(r, self.max_depth, world, lights)
                pixel_color /= self.samples_per_pixel
                color = write_color(pixel_color, self.samples_per_pixel)
                data.set_pixel(i, j, color)

        image_data_3d = data.to_3d_array()
        image = Image.new("RGB", (self.image_width, self.image_height))
        for y in range(self.image_height):
            for x in range(self.image_width):
                image.putpixel((x, y), image_data_3d[y][x])
        image.save(self.output)

    def clamp(self, v, min_v, max_v):
        return max(min(v, max_v), min_v)

    def initialize(self):
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (self.image_width / self.image_height)

        viewport_u = Vec3(viewport_width, 0, 0)
        viewport_v = Vec3(0, -viewport_height, 0)

        self.pixel_delta_u = viewport_u / self.image_width
        self.pixel_delta_v = viewport_v / self.image_height

        viewport_upper_left = self.center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2
        self.pixel00_loc = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)

    def get_ray(self, i, j):
        pixel_center = self.pixel00_loc + i * self.pixel_delta_u + j * self.pixel_delta_v
        pixel_sample = pixel_center + self.pixel_sample_square()
        ray_origin = self.center
        ray_direction = pixel_sample - ray_origin
        return Ray(ray_origin, ray_direction)

    def pixel_sample_square(self):
        px = -0.5 + random.random()
        py = -0.5 + random.random()
        return px * self.pixel_delta_u + py * self.pixel_delta_v

    def ray_color(self, r, depth, world, lights):
        rec = HitRecord()

        if world.hit(r, Interval(0.001, float('inf')), rec) and depth > 0:
            scatter_color = Vec3(0, 0, 0)
            for light in lights:
                direction_to_light = Vec3()
                is_shadowed = False

                if isinstance(light, PointLight):
                    direction_to_light = light.get_position() - rec.p
                    ray_to_light = Ray(rec.p, direction_to_light)
                    shadow_rec = HitRecord()
                    if world.hit(ray_to_light, Interval(0.001, 1.0), shadow_rec):
                        is_shadowed = True
                elif isinstance(light, ParallelLight):
                    direction_to_light = -light.get_direction()
                    ray_to_light = Ray(rec.p, direction_to_light)
                    shadow_rec = HitRecord()
                    if world.hit(ray_to_light, Interval(0.001, float('inf')), shadow_rec):
                        is_shadowed = True

                if not is_shadowed:
                    light_effect = light.illuminate(rec.p, rec.normal)
                    scattered = Ray(rec.p, rec.normal)  # Provide origin and direction
                    attenuation = Vec3()
                    if rec.mat.scatter(r, rec, attenuation, scattered, lights):
                        scatter_color += attenuation * light_effect

            return scatter_color

        return self.background_color
