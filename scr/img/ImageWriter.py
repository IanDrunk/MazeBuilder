from PIL import Image
import numpy

"""
MIT License

Copyright (c) 2019 IanDrunk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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
