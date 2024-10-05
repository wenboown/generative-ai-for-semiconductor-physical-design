import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell where the serpentine pattern will be created
cell = lib.new_cell('SERPENTINE_PATTERN')

# Parameters
width = 1.0  # Path width in µm
turns = 15  # Number of turns
segment_length = 50.0  # Length and height of each segment in µm
start_point = (0, 0)  # Starting point of the pattern
layer = 2  # GDSII layer number
datatype = 6  # GDSII datatype number

# Generate the serpentine path
path = gdspy.Path(width, start_point)
horizontal = True  # Start with horizontal segment

for turn in range(turns):
    if horizontal:
        path.segment(segment_length, '+x', layer=layer, datatype=datatype)
        path.segment(segment_length, '-y', layer=layer, datatype=datatype)
    else:
        path.segment(segment_length, '-x', layer=layer, datatype=datatype)
        path.segment(segment_length, '-y', layer=layer, datatype=datatype)
    horizontal = not horizontal

# Add the serpentine path to the cell
cell.add(path)

# Save the library to a GDSII file
lib.write_gds('serpentine_pattern.gds')

# Optionally, view the structure to verify accuracy