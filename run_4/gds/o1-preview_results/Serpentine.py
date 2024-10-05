import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Starting point
start = (0, 0)

# Path width in micrometers
path_width = 1.0  

# Create a path with the specified width starting at (0, 0)
path = gdspy.Path(path_width, start)

# Set the layer and datatype
layer = 2
datatype = 6

# Number of turns in the serpentine
num_turns = 15

# Length of each segment in micrometers
segment_length = 50.0  

# Initial direction for the horizontal segment
direction = '+x'

# Build the serpentine pattern
for i in range(num_turns):
    # Horizontal movement
    path.segment(segment_length, direction, layer=layer, datatype=datatype)
    # If not the last turn, move vertically and reverse direction
    if i < num_turns - 1:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        # Reverse horizontal direction for next segment
        direction = '-x' if direction == '+x' else '+x'

# Add the path to the cell
cell.add(path)

# Save the GDSII file
lib.write_gds('serpentine.gds')