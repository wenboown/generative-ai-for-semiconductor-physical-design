import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine')

# Define the path width, number of turns, segment length, and starting position
path_width = 1  # in microns
turns = 15
segment_length = 50  # in microns
start_position = (0, 0)

# Define the layer and datatype
layer = 2
datatype = 6

# Create the serpentine pattern
for i in range(turns):
    # Calculate the start and end positions of the current segment
    start_x = start_position[0] + (i % 2) * segment_length
    start_y = start_position[1] + (i // 2) * segment_length
    end_x = start_x + (1 - 2 * (i % 2)) * segment_length
    end_y = start_y
    
    # Create the segment as a rectangle
    segment = gdspy.Rectangle((start_x, start_y - path_width / 2), (end_x, start_y + path_width / 2), layer=layer, datatype=datatype)
    
    # Add the segment to the cell
    cell.add(segment)

# Save the design to a GDS file
lib.write_gds('serpentine.gds')