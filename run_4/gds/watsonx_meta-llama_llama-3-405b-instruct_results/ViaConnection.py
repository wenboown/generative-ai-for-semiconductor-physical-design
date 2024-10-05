import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layers
via_layer = {'layer': 1, 'datatype': 0}
metal_layer = {'layer': 2, 'datatype': 0}
pad_layer = {'layer': 3, 'datatype': 0}

# Define the via positions
via1_pos = (50, 150)
via2_pos = (550, 150)

# Define the via, pad, and metal dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600

# Create the vias
via1 = gdspy.Round(via1_pos, via_radius, **via_layer)
via2 = gdspy.Round(via2_pos, via_radius, **via_layer)

# Create the metal connection
metal_start = (via1_pos[0] - metal_width/2, via1_pos[1] - metal_width/2)
metal_end = (via2_pos[0] + metal_width/2, via2_pos[1] + metal_width/2)
metal = gdspy.Rectangle(metal_start, metal_end, **metal_layer)

# Create the pads
pad1 = gdspy.Round((via1_pos[0], via1_pos[1]), pad_radius, **pad_layer)
pad2 = gdspy.Round((via2_pos[0], via2_pos[1]), pad_radius, **pad_layer)

# Add the elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(metal)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('design.gds')