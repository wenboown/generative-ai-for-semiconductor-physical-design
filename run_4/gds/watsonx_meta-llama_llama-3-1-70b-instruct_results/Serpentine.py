import gdspy

# Parse the user's design specifications
path_width = 1  # µm
num_turns = 15
segment_length = 50  # µm
start_position = (0, 0)
layer = 2
datatype = 6

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine')

# Create the serpentine pattern
for i in range(num_turns):
    # Calculate the x and y coordinates for this segment
    if i % 2 == 0:
        x = start_position[0] + (i // 2) * segment_length
        y = start_position[1]
    else:
        x = start_position[0] + ((i - 1) // 2) * segment_length
        y = start_position[1] + segment_length
    
    # Create a rectangle for this segment
    rect = gdspy.Rectangle((x, y), (x + segment_length, y + segment_length), layer=layer, datatype=datatype)
    
    # If this is not the first segment, connect it to the previous one
    if i > 0:
        if i % 2 == 0:
            rect_start = (x, y - path_width / 2)
            rect_end = (x + path_width, y - path_width / 2)
        else:
            rect_start = (x - path_width / 2, y)
            rect_end = (x - path_width / 2, y + path_width)
        path = gdspy.Path(path_width, rect_start)
        path.segment(segment_length, '+x' if i % 2 == 0 else '+y')
        cell.add(path)
    
    # Add this segment to the cell
    cell.add(rect)

# Save the design to a GDS file
lib.write_gds('serpentine.gds')