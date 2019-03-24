from PIL import Image
import numpy


class ImageWriter:
    maze = None
    name = None
    path = None

    colors = {
        '#': 0,
        ' ': 255
    }

    def __init__(self, maze, name, path):
        self.maze = maze
        self.name = name
        self.path = path

    def get_color_matrix(self):
        matrix = list()

        for row in self.maze.layout:
            line = list()
            for cell in row:
                line.append(int(self.colors.get(cell.cellChar)))
            matrix.append(line)

        return numpy.asmatrix(matrix, dtype=numpy.uint8)

    def create_image(self):
        name = self.name
        path = self.path

        pixels = self.get_color_matrix()
        img = Image.fromarray(pixels)
        img.save(path + name + '.png')
