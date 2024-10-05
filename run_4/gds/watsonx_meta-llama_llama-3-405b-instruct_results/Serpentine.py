import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine')

# Define the layer and datatype
layer, datatype = 2, 6

# Define the path width, number of turns, and segment length
path_width = 1
num_turns = 15
segment_length = 50

# Calculate the total length and height of the serpentine pattern
total_length = segment_length * num_turns
total_height = segment_length

# Create the serpentine pattern
x, y = 0, 0
for i in range(num_turns):
    # Draw a horizontal segment
    cell.add(gdspy.Rectangle((x, y), (x + segment_length, y + path_width), layer=layer, datatype=datatype))
    x += segment_length
    
    # Draw a vertical segment
    if i % 2 == 0:
        cell.add(gdspy.Rectangle((x - path_width, y), (x, y + segment_length), layer=layer, datatype=datatype))
        y += segment_length
    else:
        cell.add(gdspy.Rectangle((x, y - segment_length), (x + path_width, y), layer=layer, datatype=datatype))
        y -= segment_length

    # Draw a horizontal segment
    if i < num_turns - 1:
        cell.add(gdspy.Rectangle((x, y), (x - segment_length, y + path_width), layer=layer, datatype=datatype))
        x -= segment_length

# Save the design to a GDS file
lib.write_gds('serpentine.gds')