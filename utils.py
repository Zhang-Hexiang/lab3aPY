import xml.etree.ElementTree as ET
from vec3 import Vec3
from light import AmbientLight, ParallelLight, PointLight
from material import PhongModel, Solid
from sphere import Sphere
from hittable_list import HittableList
from camera import Camera

def parse_scene(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    output_file = root.attrib.get("output_file", "output.png")

    # Parse background color
    bg_color_elem = root.find("background_color")
    bg_r = float(bg_color_elem.attrib.get("r", 0))
    bg_g = float(bg_color_elem.attrib.get("g", 0))
    bg_b = float(bg_color_elem.attrib.get("b", 0))
    background_color = Vec3(bg_r, bg_g, bg_b)

    # Parse camera
    camera_elem = root.find("camera")
    camera_pos_elem = camera_elem.find("position")
    cx = float(camera_pos_elem.attrib.get("x", 0))
    cy = float(camera_pos_elem.attrib.get("y", 0))
    cz = float(camera_pos_elem.attrib.get("z", 0))

    resolution_elem = camera_elem.find("resolution")
    image_width = int(resolution_elem.attrib.get("horizontal", 100))
    image_height = int(resolution_elem.attrib.get("vertical", 100))

    max_bounces_elem = camera_elem.find("max_bounces")
    max_bounces = int(max_bounces_elem.attrib.get("n", 10))

    camera = Camera()
    camera.center = Vec3(cx, cy, cz)
    camera.image_width = image_width
    camera.image_height = image_height
    camera.max_depth = max_bounces
    camera.output = output_file

    # Parse spheres
    world = HittableList()
    sphere_counter = 0
    surfaces_elem = root.find("surfaces")
    for sphere_elem in surfaces_elem.findall("sphere"):
        sphere_counter += 1
        pos_elem = sphere_elem.find("position")
        x = float(pos_elem.attrib.get("x", 0))
        y = float(pos_elem.attrib.get("y", 0))
        z = float(pos_elem.attrib.get("z", 0))
        radius = float(sphere_elem.attrib.get("radius", 1))

        material_elem = sphere_elem.find("material_solid")
        color_elem = material_elem.find("color")
        r = float(color_elem.attrib.get("r", 0))
        g = float(color_elem.attrib.get("g", 0))
        b = float(color_elem.attrib.get("b", 0))

        phong_elem = material_elem.find("phong")
        ka = float(phong_elem.attrib.get("ka", 0.1))
        kd = float(phong_elem.attrib.get("kd", 0.7))
        ks = float(phong_elem.attrib.get("ks", 0.2))
        exponent = float(phong_elem.attrib.get("exponent", 10))

        material_color = Vec3(r, g, b)
        phong = PhongModel(ka, kd, ks, exponent)
        material = Solid(material_color, phong)
        no_specular = sphere_counter == 4

        sphere = Sphere(Vec3(x, y, z), radius, material, no_specular=no_specular)
        world.add(sphere)

    # Parse lights
    lights = []
    lights_elem = root.find("lights")

    # Parse ambient light
    ambient_light_elem = lights_elem.find("ambient_light")
    if ambient_light_elem is not None:
        color_elem = ambient_light_elem.find("color")
        r = float(color_elem.attrib.get("r", 1.0))
        g = float(color_elem.attrib.get("g", 1.0))
        b = float(color_elem.attrib.get("b", 1.0))
        intensity = float(ambient_light_elem.attrib.get("intensity", 2.5))
        ambient_light = AmbientLight(Vec3(r, g, b), intensity)
        lights.append(ambient_light)

    # Parse parallel light
    for parallel_light_elem in lights_elem.findall("parallel_light"):
        color_elem = parallel_light_elem.find("color")
        direction_elem = parallel_light_elem.find("direction")
        r = float(color_elem.attrib.get("r", 0))
        g = float(color_elem.attrib.get("g", 0))
        b = float(color_elem.attrib.get("b", 0))
        x = float(direction_elem.attrib.get("x", 0))
        y = float(direction_elem.attrib.get("y", 0))
        z = float(direction_elem.attrib.get("z", 0))
        intensity = float(parallel_light_elem.attrib.get("intensity", 2.5))
        parallel_light = ParallelLight(Vec3(x, y, z), Vec3(r, g, b), intensity)
        lights.append(parallel_light)

    return output_file, background_color, camera, lights, world, image_width, image_height, max_bounces
