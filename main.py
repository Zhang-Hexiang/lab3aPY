from utils import parse_scene
from camera import Camera

def render_scene(xml_file, output_file):
    output_file, background_color, camera, lights, world, image_width, image_height, max_bounces = parse_scene(xml_file)
    camera.output = output_file  # Set the output file name
    camera.background_color = background_color
    camera.image_width = image_width
    camera.image_height = image_height
    camera.max_depth = max_bounces
    camera.render(world, lights)

def main():
    # Render example1.xml
    render_scene('example1.xml', 'example1.png')
    print("example1 output completed")
    # Render example2.xml
    render_scene('example2.xml', 'example2.png')
    print("example2 output completed")
    # Render example3.xml
    render_scene('example3.xml', 'example3.png')
    print("example3 output completed")

if __name__ == '__main__':
    main()
