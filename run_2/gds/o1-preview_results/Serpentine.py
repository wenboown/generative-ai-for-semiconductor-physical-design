import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('SERPENTINE')

# Specifications
path_width = 1.0  # µm
num_turns = 15
segment_length = 50.0  # µm
start_point = (0, 0)
layer = 2
datatype = 6

# Initialize the path at start_point with path_width
path = gdspy.Path(path_width, start_point)

# Determine the number of repeats and any remaining turns
turns_per_repeat = 3  # Number of turns in each repeat unit
num_repeats = num_turns // turns_per_repeat
remaining_turns = num_turns % turns_per_repeat

direction = '+x'  # Initial horizontal direction

for _ in range(num_repeats):
    # Horizontal segment
    path.segment(segment_length, direction, layer=layer, datatype=datatype)
    # Vertical segment (up)
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)
    # Switch horizontal direction
    direction = '-x' if direction == '+x' else '+x'
    # Horizontal segment
    path.segment(segment_length, direction, layer=layer, datatype=datatype)
    # Vertical segment (up)
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)
    # Switch horizontal direction
    direction = '-x' if direction == '+x' else '+x'
    # Horizontal segment
    path.segment(segment_length, direction, layer=layer, datatype=datatype)
    # Vertical segment (up)
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)
    # Switch horizontal direction for the next repeat
    direction = '-x' if direction == '+x' else '+x'

# Add any remaining turns
if remaining_turns > 0:
    # Horizontal segment
    path.segment(segment_length, direction, layer=layer, datatype=datatype)
    # Vertical segment (up)
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)
    # Switch horizontal direction
    direction = '-x' if direction == '+x' else '+x'
    remaining_turns -= 1
    if remaining_turns > 0:
        # Horizontal segment
        path.segment(segment_length, direction, layer=layer, datatype=datatype)
        # Vertical segment (up)
        path.segment(segment_length, '+y', layer=layer, datatype=datatype)
        # Switch horizontal direction
        direction = '-x' if direction == '+x' else '+x'

# Add the path to the cell
cell.add(path)

# Save the GDSII file
lib.write_gds('serpentine.gds')