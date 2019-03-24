import os
import sys
import random

from scr.Maze import Maze
from scr.ImageWriter import ImageWriter

# Constants
ARG_COUNT = 3
MAZE_MIN_SIZE = 12
MAZE_MAX_SIZE = 64

# Store maze settings
size = 0
name = ''

# Read arguments from command and Validate data
if len(sys.argv) != ARG_COUNT:
    print("Input correct arguments:"
          "\n  [1]: size of maze (" + str(MAZE_MIN_SIZE) + "-" + str(MAZE_MAX_SIZE) + ")"
          "\n  [2]: maze file name (w/o extension, [0-9; a-z])")
    exit()
else:
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("Size must be an integer. Try again")
        exit()
    name = str(sys.argv[2])

if not MAZE_MIN_SIZE <= size <= MAZE_MAX_SIZE:
    print('Maze size must be from ' + str(MAZE_MIN_SIZE) + " to " + str(MAZE_MAX_SIZE) + "!")
    exit()
if not name.isalnum():
    print('Maze name must contain only digits and/or letters!')
    exit()

# We will use only odd numbers for our mazes
# So if size is even - we reduce it by one
if size % 2 == 0:
    size -= 1

# Create empty maze and start building it
maze = Maze(size)

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
