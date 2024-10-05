import gdspy

# Define the design parameters
path_width = 1
num_turns = 15
segment_length = 50
segment_height = 50
start_position = (0, 0)
layer = 2
datatype = 6

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine_pattern')

# Initialize the current position
x, y = start_position

# Draw the serpentine pattern
for i in range(num_turns):
    # Draw a horizontal segment
    rect = gdspy.Rectangle((x, y), (x + segment_length, y + path_width), layer=layer, datatype=datatype)
    cell.add(rect)
    x += segment_length
    
    # Draw a vertical segment
    rect = gdspy.Rectangle((x, y), (x + path_width, y + segment_height), layer=layer, datatype=datatype)
    cell.add(rect)
    y += segment_height
    
    # Draw a horizontal segment
    rect = gdspy.Rectangle((x, y), (x - segment_length, y + path_width), layer=layer, datatype=datatype)
    cell.add(rect)
    x -= segment_length
    
    # Draw a vertical segment
    rect = gdspy.Rectangle((x, y), (x - path_width, y + segment_height), layer=layer, datatype=datatype)
    cell.add(rect)
    y += segment_height

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')