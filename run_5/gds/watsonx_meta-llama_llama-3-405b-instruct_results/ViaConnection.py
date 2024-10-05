import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layers
via_layer = {'layer': 0, 'datatype': 0}
metal_layer = {'layer': 1, 'datatype': 0}
pad_layer = {'layer': 2, 'datatype': 0}

# Define the via positions
via1_pos = (50, 150)
via2_pos = (550, 150)

# Create vias
via1 = gdspy.Round((via1_pos[0], via1_pos[1]), 10, **via_layer)
via2 = gdspy.Round((via2_pos[0], via2_pos[1]), 10, **via_layer)

# Create pads
pad1 = gdspy.Round((via1_pos[0], via1_pos[1]), 30, **pad_layer)
pad2 = gdspy.Round((via2_pos[0], via2_pos[1]), 30, **pad_layer)

# Create metal connection
metal_width = 40
metal_length = 600
metal_margin = 10
via_to_metal_margin = 50
metal_start_x = via1_pos[0] - via_to_metal_margin
metal_end_x = via2_pos[0] + via_to_metal_margin
metal = gdspy.Rectangle((metal_start_x, via1_pos[1] - metal_width/2),
                        (metal_end_x, via1_pos[1] + metal_width/2), **metal_layer)

# Add elements to the cell
cell.add([via1, via2, pad1, pad2, metal])

# Save the design to a GDS file
lib.write_gds('design.gds')