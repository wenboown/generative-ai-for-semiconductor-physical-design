import gdspy

# Parameters
path_width = 1.0  # µm
turns = 15
segment_length = 50.0  # µm
start_point = (0, 0)
layer = 2
datatype = 6

# Create the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SERPENTINE_PATTERN')

# Create the serpentine path
path = gdspy.Path(path_width, start_point)
direction = '+x'
for i in range(turns):
    if direction == '+x':
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)
        direction = '+y'
    elif direction == '+y':
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        direction = '-x'
    elif direction == '-x':
        path.segment(segment_length, '-x', layer=layer, datatype=datatype)
        direction = '+y'
    elif direction == '+y':
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        direction = '+x'
    # Alternate direction to create turns

    if i % 2 == 0:
        direction = '+x' if direction == '-x' else '-x'
    else:
        direction = '+y' if direction == '-y' else '-y'

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')

# Optionally, display layout using gdspy internal viewer