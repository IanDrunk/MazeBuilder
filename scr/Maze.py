import random
import sys

"""
This class represents a maze instance
"""


# Maze class itself
class Maze:
    size = 0
    layout = list()

    def __init__(self, dimensions):
        layout = self.layout
        self.size = dimensions

        # Build initial layout
        for xx in range(dimensions):
            row = list()
            for yy in range(dimensions):
                node = Node(xx, yy)
                node.x = xx
                node.y = yy

                # As we are operating in 2D there is only 4 possible directions:
                # UP, LEFT, DOWN, RIGHT. We'll represent it in binary as [0b U L D R]
                node.directions = 0b1111

                if xx * yy % 2 == 1:
                    node.set_type('air')
                else:
                    node.set_type('wall')

                # Create node and add it to layout row
                row.append(node)

            # Add filled row to maze layout
            layout.append(row)

        # Define starting point
        start = layout[1][1]
        start.parent = start
        last = start

        # Link all the nodes (cells) into paths
        while True:
            last = last.link(self)
            if last == start:
                break

    # Print function for visual indication of maze structure
    def print_maze(self):
        for row in self.layout:
            for cell in row:
                sys.stdout.write(cell.get_node_char() + ' ')
            print()


# Represents single node in the maze
class Node:
    x = -1
    y = -1
    parent = None
    directions = 0b1111

    cellType = 'wall'
    cellChar = '#'
    charForType = {
        'wall': '#',
        'air': ' '
    }

    def __init__(self, x, y):
        self.coord = (int(x), int(y))

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

        # While we have where to go
        while self.directions > 0:
            # Get random direction
            dirs = [0b1000, 0b0100, 0b0010, 0b0001]
            n_dir = random.choice(dirs)

            # Check if it is unexplored yet
            if self.directions & (~n_dir) < self.directions:

                # Update directions
                self.directions = self.directions & (~n_dir)

                # Check if it's possible to go right
                if n_dir == 1:
                    if self.x + 2 < maze.size:
                        x = self.x + 2
                        y = self.y

                # Check if it's possible to go down
                elif n_dir == 2:
                    if self.y + 2 < maze.size:
                        x = self.x
                        y = self.y + 2

                # Check if it's possible to go left
                elif n_dir == 4:
                    if self.x - 2 >= 0:
                        x = self.x - 2
                        y = self.y

                # Check if it's possible to go up
                elif n_dir == 8:
                    if self.y - 2 >= 0:
                        x = self.x
                        y = self.y - 2

            else:
                continue

            # Make sure that destination cell is not a wall
            destination = maze.layout[x][y]
            if destination.cellChar is ' ':

                # If destination is a linked node already - abort
                if destination.parent is not None:
                    continue

                # Otherwise, adopt node
                destination.parent = self

                # Remove wall between nodes
                xx = int(self.x + (x - self.x) / 2)
                yy = int(self.y + (y - self.y) / 2)
                in_between_node = maze.layout[xx][yy]
                in_between_node.set_type('air')

                # Return address of the child node
                return destination

        return self.parent
