from vec3 import Vec3

Color = Vec3

def write_color(pixel_color, samples_per_pixel):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()
    # Apply gamma correction and scale by number of samples
    scale = 1.0 / samples_per_pixel
    r = r * scale
    g = g * scale
    b = b * scale
    return (int(255.999 * r), int(255.999 * g), int(255.999 * b))
