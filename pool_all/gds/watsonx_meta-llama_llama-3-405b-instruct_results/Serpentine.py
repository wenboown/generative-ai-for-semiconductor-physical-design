import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell where the serpentine pattern will be created
cell = lib.new_cell('SERPENTINE_PATTERN')

# Parameters
path_width = 1.0  # Path width in micrometers
turns = 15  # Number of turns
segment_length = 50.0  # Length and height of each segment in micrometers
start_point = (0, 0)  # Starting point of the pattern
layer = 2  # GDSII layer number
datatype = 6  # GDSII datatype number

# Initialize the path
path = gdspy.Path(path_width, start_point)

# Generate the serpentine path
for i in range(turns):
    if i % 2 == 0:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)
    else:
        path.segment(segment_length, '-y', layer=layer, datatype=datatype)
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)

# Add the path to the cell
cell.add(path)

# Save the library to a GDSII file
lib.write_gds('serpentine_pattern.gds')