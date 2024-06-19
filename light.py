from vec3 import Vec3

class Light:
    def illuminate(self, p, normal):
        raise NotImplementedError

class AmbientLight(Light):
    def __init__(self, color, intensity=1.0):
        self.ambient_color = color * intensity

    def illuminate(self, p, normal):
        return self.ambient_color

class ParallelLight(Light):
    def __init__(self, direction, color, intensity=1.0):
        self.direction = Vec3.unit_vector(direction)
        self.light_color = color * intensity

    def get_direction(self):
        return self.direction

    def illuminate(self, p, normal):
        intensity = max(Vec3.dot(-self.direction, normal), 0.0)
        return intensity * self.light_color

class PointLight(Light):
    def __init__(self, position, color, intensity=1.0):
        self.position = position
        self.light_color = color * intensity

    def get_position(self):
        return self.position

    def illuminate(self, p, normal):
        light_dir = Vec3.unit_vector(self.position - p)
        intensity = max(Vec3.dot(normal, light_dir), 0.0)
        return intensity * self.light_color
