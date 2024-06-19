from vec3 import Vec3
from ray import Ray
from light import AmbientLight, ParallelLight, PointLight

class Material:
    def scatter(self, r_in, rec, attenuation, scattered, lights):
        raise NotImplementedError

class PhongModel:
    def __init__(self, ka, kd, ks, exponent):
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.exponent = exponent

class Solid(Material):
    def __init__(self, a, phong):
        self.albedo = a  # color
        self.phong = phong  # Phong model parameter

    def scatter(self, r_in, rec, attenuation, scattered, lights):
        view_dir = Vec3.unit_vector(-r_in.directionPos)  # view direction
        normal = rec.normal  # normal

        #initialization
        ambient = Vec3(0, 0, 0)
        diffuse = Vec3(0, 0, 0)
        specular = Vec3(0, 0, 0)

        for light in lights:
            light_effect = light.illuminate(rec.p, normal)  # Calculating lighting effects

            if isinstance(light, AmbientLight):
                ambient += light_effect * self.phong.ka  # Calculate ambient light component
            else:
                light_dir = Vec3()
                if isinstance(light, ParallelLight):
                    light_dir = Vec3.unit_vector(-light.get_direction())
                elif isinstance(light, PointLight):
                    light_dir = Vec3.unit_vector(light.get_position() - rec.p)

                diff_intensity = max(Vec3.dot(light_dir, normal), 0.0)
                diffuse += light_effect * diff_intensity * self.phong.kd  # Calculate the diffuse light component

                if not rec.no_specular:
                    reflect_dir = Vec3.reflect(-light_dir, normal)  # Reflection direction
                    spec_intensity = pow(max(Vec3.dot(view_dir, reflect_dir), 0.0), self.phong.exponent)
                    specular += light_effect * spec_intensity * self.phong.ks  # Calculate the highlight component

        combined_color = ambient + diffuse + specular  # Composite Color
        attenuation.e = (combined_color * self.albedo).e  # Applying color and lighting
        scattered.originPos = rec.p  # Update the starting point of the ray
        scattered.directionPos = rec.normal  # Update the direction of the light

        return True
