import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell for our design
cell = lib.new_cell('SERPENTINE_PATTERN')

# Define the serpentine pattern parameters
path_width = 1.0  # micrometers
num_turns = 15
segment_length = 50.0  # micrometers
start_point = (0, 0)
layer = 2
datatype = 6

# Create the serpentine path
path = gdspy.Path(path_width, start_point)

# Draw the serpentine pattern
for i in range(num_turns):
    if i % 2 == 0:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)
    else:
        path.segment(segment_length, '-y', layer=layer, datatype=datatype)
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)

# Adding the path to the cell
cell.add(path)

# Write the GDS file
lib.write_gds('serpentine_pattern.gds')

# Optionally, display using an internal viewer