import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SERPENTINE_PATTERN')

# Parameters for serpentine pattern
path_width = 1.0
turns = 15
segment_length = 50.0
start_point = (0, 0)
layer = 2
datatype = 6

# Create the initial Path object
path = gdspy.Path(path_width, start_point)

# Add segments to the path to create the serpentine pattern
for i in range(turns):
    if i % 2 == 0:
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
    else:
        path.segment(segment_length, '-y', layer=layer, datatype=datatype)
    path.segment(segment_length, '+x', layer=layer, datatype=datatype)

# Add the final vertical segment to complete the shape
if turns % 2 == 0:
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)
else:
    path.segment(segment_length, '-y', layer=layer, datatype=datatype)

# Add the path into the cell
cell.add(path)

# Write the GDS file
lib.write_gds('serpentine_pattern.gds')

# Optional: to view the layout using gdspy internal viewer