import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell where the serpentine pattern will be created
cell = lib.new_cell('serpentine')

# Define the path width, number of turns, and segment length
path_width = 1.0  # micrometers
num_turns = 15
segment_length = 50.0  # micrometers
starting_point = (0, 0)

# Define the layer and datatype
layer = 2
datatype = 6

# Initialize the path
path = gdspy.Path(path_width, starting_point)

# Generate the serpentine pattern
direction = '+x'
for i in range(num_turns):
    if i % 2 == 0:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)
    else:
        path.segment(segment_length, '-y', layer=layer, datatype=datatype)
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)

# Add the path to the cell
cell.add(path)

# Save the library to a GDS file
lib.write_gds('serpentine_pattern.gds')