import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SERPENTINE')

# Define parameters
path_width = 1  # 1 µm
num_turns = 15
segment_length = 50  # 50 µm
layer = 2
datatype = 6

# Create the serpentine path
path = gdspy.FlexPath([(0, 0)], path_width, layer=layer, datatype=datatype)

for i in range(num_turns):
    # Vertical segment
    path.segment(segment_length, '+y')
    
    # Horizontal segment
    direction = '+x' if i % 2 == 0 else '-x'
    path.segment(segment_length, direction)

# Add the final vertical segment to complete the pattern
path.segment(segment_length, '+y')

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')

print("Serpentine pattern has been generated and saved to 'serpentine_pattern.gds'.")