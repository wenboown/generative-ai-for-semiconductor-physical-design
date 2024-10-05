import gdspy

def generate_serpentine_pattern(path_width, num_turns, segment_length, layer, datatype):
    # Create a new library and cell
    lib = gdspy.GdsLibrary()
    cell = lib.new_cell('serpentine_pattern')

    # Initialize the starting point
    x, y = 0, 0

    # Create the serpentine pattern
    for i in range(num_turns):
        # Draw the horizontal segment
        rect = gdspy.Rectangle((x, y), (x + segment_length, y + path_width), layer=layer, datatype=datatype)
        cell.add(rect)

        # Move to the next segment
        x += segment_length
        y = -y - segment_length if i % 2 == 0 else -y + segment_length

        # Draw the vertical segment
        rect = gdspy.Rectangle((x, y), (x + path_width, y + segment_length), layer=layer, datatype=datatype)
        cell.add(rect)

        # Move to the next segment
        x = -x - path_width if i % 2 == 0 else -x + path_width

    # Save the design to a GDS file
    lib.write_gds('serpentine_pattern.gds')

# Generate the serpentine pattern with the specified parameters
generate_serpentine_pattern(1, 15, 50, 2, 6)