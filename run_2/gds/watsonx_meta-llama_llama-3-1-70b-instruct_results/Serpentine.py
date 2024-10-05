import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('serpentine_pattern')

# Define the path width, number of turns, segment length, and layer/datatype
path_width = 1
num_turns = 15
segment_length = 50
layer = 2
datatype = 6

# Initialize the current position
x, y = 0, 0

# Create the serpentine pattern
for i in range(num_turns):
    # Draw the horizontal segment
    points = [(x, y), (x + segment_length, y)]
    cell.add(gdspy.Path(path_width, points, layer=layer, datatype=datatype))

    # Update the current position
    x += segment_length
    y += path_width

    # Draw the vertical segment
    points = [(x, y), (x, y + segment_length)]
    cell.add(gdspy.Path(path_width, points, layer=layer, datatype=datatype))

    # Update the current position
    y += segment_length
    x -= segment_length

    # Repeat the pattern for the remaining turns
    if i < num_turns - 1:
        # Draw the horizontal segment
        points = [(x, y), (x - segment_length, y)]
        cell.add(gdspy.Path(path_width, points, layer=layer, datatype=datatype))

        # Update the current position
        x -= segment_length
        y -= path_width

        # Draw the vertical segment
        points = [(x, y), (x, y - segment_length)]
        cell.add(gdspy.Path(path_width, points, layer=layer, datatype=datatype))

        # Update the current position
        y -= segment_length
        x += segment_length

# Save the design to a GDS file
lib.write_gds('serpentine_pattern.gds')