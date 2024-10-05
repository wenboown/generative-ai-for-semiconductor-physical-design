import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a GDSII cell
cell = lib.new_cell('SERPENTINE_PATTERN')

# Starting point coordinates
x0, y0 = 0, 0

# Define path parameters
path_width = 1.0            # Path width of 1 µm
turns = 15                  # Number of turns
segment_length = 50.0       # Each segment is 50 µm long and tall

# Initialize the path at the starting point
path = gdspy.Path(path_width, (x0, y0))

# Start by moving right by one segment length
path.segment(segment_length, '+x', layer=2, datatype=6)

# Generate the serpentine pattern
for i in range(turns):
    # Move up by one segment length
    path.segment(segment_length, '+y', layer=2, datatype=6)
    if i % 2 == 0:
        # On even turns, move left
        path.segment(segment_length, '-x', layer=2, datatype=6)
    else:
        # On odd turns, move right
        path.segment(segment_length, '+x', layer=2, datatype=6)

# Add the path to the cell
cell.add(path)

# Save the library to a GDSII file
lib.write_gds('serpentine_pattern.gds')