import os
import sys
import random

from scr.Maze import Maze
from scr.img.ImageWriter import ImageWriter

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


# Constants
ARG_COUNT = 4
MAZE_MIN_SIZE = 12
MAZE_MAX_SIZE = 64
OUTPUT_MODES = "pic", "2d", "3d"

# Store maze settings
size = 0
name = ''
mode = None

# Read arguments from command and Validate data
if len(sys.argv) != ARG_COUNT:
    print("Input correct arguments:"
          "\n  [1]: maze file name (w/o extension, [0-9; a-z])"
          "\n  [2]: size of maze (" + str(MAZE_MIN_SIZE) + "-" + str(MAZE_MAX_SIZE) + ")"
          "\n  [3]: output mode " + str(OUTPUT_MODES))

    exit()
else:
    try:
        size = int(sys.argv[2])
    except ValueError:
        print("Size must be an integer. Try again")
        exit()
    name = str(sys.argv[1])
    mode = str(sys.argv[3])
if not MAZE_MIN_SIZE <= size <= MAZE_MAX_SIZE:
    print('Maze size must be from ' + str(MAZE_MIN_SIZE) + " to " + str(MAZE_MAX_SIZE) + "!")
    exit()
if not name.isalnum():
    print('Maze name must contain only digits and/or letters!')
    exit()
if mode not in OUTPUT_MODES:
    print('Output mode must be one of ' + str(OUTPUT_MODES) + '!')
    exit()

# TODO: remove in implementation
if mode is not 'pic':
    print('Sorry. Not implemented yet...')
    exit()

# We will use only odd numbers for our mazes
# So if size is even - we reduce it by one
if size % 2 == 0:
    size -= 1

# Create empty maze and start building it
maze = Maze(size, mode)

# Create start cell at the random position at the top
start_y = random.randrange(size)
if start_y % 2 == 0:
    if start_y == 0:
        start_y += 1
    else:
        start_y -= 1
maze.layout[0][start_y].set_type('air')

# Create end cell at the random position at the bottom
end_y = random.randrange(size)
if end_y % 2 == 0:
    if end_y == 0:
        end_y += 1
    else:
        end_y -= 1
maze.layout[size - 1][end_y].set_type('air')

# Check if out folder exists, else - create it
path = os.path.dirname(os.path.realpath(__file__)) + '/out/'
if not os.path.exists(path):
    os.makedirs(path)

# Save maze as png
iw = ImageWriter(maze, name, path)
iw.create_image()

# maze.print_maze()

# End of script
exit()
