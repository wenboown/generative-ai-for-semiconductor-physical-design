import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to hold the serpentine pattern
cell = lib.new_cell('SERPENTINE')

# Define the path parameters
path_width = 1.0  # Path width in micrometers
num_turns = 15    # Number of turns
segment_length = 50.0  # Length of each segment in micrometers
start_position = (0, 0)  # Starting point of the path
layer = 2         # Layer number
datatype = 6      # Datatype

# Create the initial path
path = gdspy.Path(path_width, start_position)

# Build the serpentine pattern
for i in range(num_turns):
    # Alternate direction for each horizontal segment
    direction = '+x' if i % 2 == 0 else '-x'
    path.segment(segment_length, direction, layer=layer, datatype=datatype)
    # Add vertical segment between horizontal segments except after the last turn
    if i < num_turns - 1:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)

# Add the path to the cell
cell.add(path)

# Save the GDSII file
lib.write_gds('serpentine.gds')