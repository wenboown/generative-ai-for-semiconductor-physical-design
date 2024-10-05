import gdspy

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SERPENTINE')

# Define the path parameters
path_width = 1.0  # µm
num_turns = 15
segment_length = 50.0  # µm
start_point = (0, 0)
layer = 2
datatype = 6

# Create the path
path = gdspy.Path(path_width, start_point)

for i in range(num_turns):
    # Determine direction
    if i % 2 == 0:
        # Even turn: move right
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)
    else:
        # Odd turn: move left
        path.segment(segment_length, '-x', layer=layer, datatype=datatype)
    # Move up after each horizontal segment, except after the last one
    if i != num_turns - 1:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('serpentine.gds')