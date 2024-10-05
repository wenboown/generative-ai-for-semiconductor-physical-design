import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine')

# Define the path width, number of turns, segment length, and start position
width = 1  # in micrometers
turns = 15
segment_length = 50  # in micrometers
start_pos = (0, 0)

# Initialize the path
path = gdspy.Path(width, start_pos)

# Create the serpentine pattern
for i in range(turns):
    # Move up
    path.segment(segment_length, direction='+y', layer=2, datatype=6)
    # Move right
    if i % 2 == 0:
        path.segment(segment_length, direction='+x', layer=2, datatype=6)
    # Move left
    else:
        path.segment(segment_length, direction='-x', layer=2, datatype=6)
    # Move down
    path.segment(segment_length, direction='-y', layer=2, datatype=6)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('serpentine.gds')