import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("serpentine")

# Define the layer and datatype
layer = 2
datatype = 6

# Define the path width and segment length
path_width = 1
segment_length = 50

# Calculate the number of segments per turn
segments_per_turn = 2

# Calculate the total number of segments
total_segments = 15 * segments_per_turn

# Define the starting point
x, y = 0, 0

# Create the serpentine pattern
for i in range(total_segments):
    # Determine the direction of the segment (horizontal or vertical)
    if i % segments_per_turn == 0:
        # Change direction (90-degree turn)
        direction = 'h' if (i // segments_per_turn) % 2 == 0 else 'v'
    else:
        # Continue in the current direction
        direction = 'h' if direction == 'h' else 'v'

    # Draw the segment
    if direction == 'h':
        cell.add(gdspy.Rectangle((x, y), (x + segment_length, y + path_width), layer=layer, datatype=datatype))
        x += segment_length
    else:
        cell.add(gdspy.Rectangle((x, y), (x + path_width, y + segment_length), layer=layer, datatype=datatype))
        y += segment_length

# Save the design to a GDS file
lib.write_gds("serpentine.gds")