import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define a cell for the layout
cell = lib.new_cell('SERPENTINE')

# Parameters for the serpentine path
path_width = 1
num_turns = 15
segment_length = 50
start_x = 0
start_y = 0
layer = 2
datatype = 6

# Initialize the path
path = gdspy.Path(width=path_width, initial_point=(start_x, start_y))

# Alternate horizontal and vertical segments to create the serpentine pattern
for i in range(num_turns):
    direction = 1 if i % 2 == 0 else -1  # Alternate direction
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)
    path.segment(segment_length * direction, '+x', layer=layer, datatype=datatype)

# Ensure the final vertical segment if num_turns is even
if num_turns % 2 == 0:
    path.segment(segment_length, '+y', layer=layer, datatype=datatype)

# Add the path to the cell
cell.add(path)

# Save the library to a GDS file
lib.write_gds('serpentine_pattern.gds')

# Optionally, view the design (requires a graphical front-end)