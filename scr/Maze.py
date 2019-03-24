import random
import sys

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


# Maze class itself
class Maze:
    size = 0
    layout = list()
    mode = ''

    def __init__(self, dimensions, mode='pic'):
        layout = self.layout
        self.size = dimensions
        self.mode = mode

        # Build initial layout
        for zz in range(dimensions):
            layer = list()
            for xx in range(dimensions):
                row = list()
                for yy in range(dimensions):
                    node = Node(xx, yy, zz)
                    node.x = xx
                    node.y = yy
                    node.z = zz

                    # As we are operating in 2D there is only 4 possible directions:
                    # UP, DOWN, NORTH, WEST, SOUTH, EAST. We'll represent it in binary as [0b U D N W S E]
                    node.directions = 0b111111

                    if xx * yy * zz % 3 == 1:
                        node.set_type('air')
                    else:
                        node.set_type('wall')

                    # Create node and add it to layout row
                    row.append(node)

                # Add filled row to maze layout
                layer.append(row)

            # Add filled layer to the maze layout
            layout.append(layer)

        # Define starting point
        start = layout[1][1][1]
        start.parent = start
        last = start

        # Link all the nodes (cells) into paths
        while True:
            last = last.link(self)
            if last == start:
                break

    # Print function for visual indication of maze structure
    def print_maze_2d(self):
        if self.mode is not '3d':
            for row in self.layout:
                for cell in row:
                    sys.stdout.write(cell.get_node_char() + ' ')
                print()


# Represents single node in the maze
class Node:
    x = -1
    y = -1
    z = -1
    is3d = False
    parent = None
    directions = 0b111111

    cellType = 'wall'
    cellChar = '#'
    charForType = {
        'wall': '#',
        'air': ' '
    }

    def __init__(self, x, y, z=999):
        self.coord = (int(x), int(y), int(z))
        if z == 999:
            self.is3d = True

    def get_node_char(self):
        return self.cellChar

    def set_type(self, set_to_type):
        self.cellType = set_to_type
        self.cellChar = self.charForType.get(set_to_type)

    # Connects node to random neighbor( if possible) and returns
    # address of next node that should be visited
    def link(self, maze):

        # Safety check
        if self is None:
            return

        x = self.x
        y = self.y
        z = self.z

        # While we have where to go
        while self.directions > 0:
            # Get random direction
            dirs = [0b100000, 0b010000, 0b001000, 0b000100, 0b000010, 0b000001]
            n_dir = random.choice(dirs)

            # Check if it is unexplored yet
            if self.directions & (~n_dir) < self.directions:

                # Update directions
                self.directions = self.directions & (~n_dir)

                # Check if it's possible to go EAST
                if n_dir == 1:
                    if self.x + 2 < maze.size:
                        x = self.x + 2
                        y = self.y

                # Check if it's possible to go SOUTH
                elif n_dir == 2:
                    if self.y + 2 < maze.size:
                        x = self.x
                        y = self.y + 2

                # Check if it's possible to go WEST
                elif n_dir == 4:
                    if self.x - 2 >= 0:
                        x = self.x - 2
                        y = self.y

                # Check if it's possible to go NORTH
                elif n_dir == 8:
                    if self.y - 2 >= 0:
                        x = self.x
                        y = self.y - 2

                # FOR 3D MAZES ONLY
                # Check if it's possible to go UP
                elif n_dir == 16 and self.is3d:
                    if self.z - 2 >= 0:
                        x = self.x
                        y = self.y
                        z = self.z - 2

                # Check if it's possible to go DOWN
                elif n_dir == 32 and self.is3d:
                    if self.z + 2 < maze.size:
                        x = self.x
                        y = self.y
                        z = self.z + 2

            else:
                continue

            # Make sure that destination cell is not a wall
            destination = maze.layout[x][y][z]
            if destination.cellChar is ' ':

                # If destination is a linked node already - abort
                if destination.parent is not None:
                    continue

                # Otherwise, adopt node
                destination.parent = self

                # Remove wall between nodes
                xx = int(self.x + (x - self.x) / 2)
                yy = int(self.y + (y - self.y) / 2)
                zz = int(self.z + (z - self.z) / 2)
                in_between_node = maze.layout[xx][yy][zz]
                in_between_node.set_type('air')

                # Return address of the child node
                return destination

        return self.parent
