import gdspy

# Define the GDS cell
cell = gdspy.Cell('SERPENTINE_PATTERN')

# Define the path parameters
path_width = 1
layer = 2
datatype = 6
turns = 15
segment_length = 50

# Define the initial position
x, y = 0, 0

# Create the serpentine path
for i in range(turns):
    # Create a horizontal segment
    rect = gdspy.Rectangle((x, y), (x + segment_length, y + path_width), layer=layer, datatype=datatype)
    cell.add(rect)
    x += segment_length
    
    # Create a vertical segment
    rect = gdspy.Rectangle((x, y), (x + path_width, y + segment_length), layer=layer, datatype=datatype)
    cell.add(rect)
    y += segment_length
    
    # Create a horizontal segment
    rect = gdspy.Rectangle((x, y), (x - segment_length, y + path_width), layer=layer, datatype=datatype)
    cell.add(rect)
    x -= segment_length
    
    # Create a vertical segment
    rect = gdspy.Rectangle((x, y), (x - path_width, y + segment_length), layer=layer, datatype=datatype)
    cell.add(rect)
    y += segment_length

# Save the GDS file
gdspy.write_gds('serpentine_pattern.gds', cells=[cell])