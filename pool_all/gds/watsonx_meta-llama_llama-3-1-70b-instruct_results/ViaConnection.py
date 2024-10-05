import gdspy

# Define the layers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Define the dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600

# Define the positions of the vias
via1_position = (50, 150)
via2_position = (550, 150)

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Create the vias
via1 = gdspy.Round(via1_position, via_radius, layer=via_layer)
via2 = gdspy.Round(via2_position, via_radius, layer=via_layer)
cell.add(via1)
cell.add(via2)

# Create the pads
pad1 = gdspy.Round(via1_position, pad_radius, layer=pad_layer)
pad2 = gdspy.Round(via2_position, pad_radius, layer=pad_layer)
cell.add(pad1)
cell.add(pad2)

# Calculate the metal connection coordinates
metal_x1 = via1_position[0] - 50
metal_x2 = via2_position[0] + 50
metal_y1 = via1_position[1] - metal_width / 2
metal_y2 = via1_position[1] + metal_width / 2

# Create the metal connection
metal = gdspy.Rectangle((metal_x1, metal_y1), (metal_x2, metal_y2), layer=metal_layer)
cell.add(metal)

# Save the design to a GDS file
lib.write_gds('layout.gds')