import sys

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

# TODO: Create empty maze and start building it
# TODO: Save maze as png

# End of script
exit()
