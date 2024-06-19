class ImageData:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        # Initialize a completely black image data array
        self.data = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        """Sets the color of the specified pixel"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.data[y][x] = [int(c) for c in color]

    def get_pixel(self, x, y):
        """Get the color of the specified pixel"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.data[y][x]
        return [0, 0, 0]  # default color is black

    def to_3d_array(self):
        """Convert image data into a three-dimensional list suitable for PIL processing"""
        height, width = self.height, self.width
        array = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(tuple(self.data[y][x]))
            array.append(row)
        return array
