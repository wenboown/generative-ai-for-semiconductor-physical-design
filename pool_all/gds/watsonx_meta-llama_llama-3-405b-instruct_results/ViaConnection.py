import gdspy

# Create a library
lib = gdspy.GdsLibrary()

# Create a cell in the library
cell = lib.new_cell('LAYOUT')

# Define the layers
VIA_LAYER = 1
METAL_LAYER = 2
PAD_LAYER = 3

# Define the specifications
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
margin = 10
space_from_via_to_edge = 50

# Define positions for vias
via1_center = (50, 150)
via2_center = (550, 150)

# Create the vias
via1 = gdspy.Round(via1_center, via_radius, layer=VIA_LAYER)
via2 = gdspy.Round(via2_center, via_radius, layer=VIA_LAYER)

# Create the pads
pad1 = gdspy.Round(via1_center, pad_radius, layer=PAD_LAYER)
pad2 = gdspy.Round(via2_center, pad_radius, layer=PAD_LAYER)

# Define the coordinates for the metal connection
metal_left_x = via1_center[0] - space_from_via_to_edge
metal_right_x = via2_center[0] + space_from_via_to_edge
metal_y_bottom = via1_center[1] - metal_width / 2
metal_y_top = via1_center[1] + metal_width / 2

# Create the metal connection
metal = gdspy.Rectangle((metal_left_x, metal_y_bottom), (metal_right_x, metal_y_top), layer=METAL_LAYER)

# Add elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(pad1)
cell.add(pad2)
cell.add(metal)

# Save the design to a GDS file
lib.write_gds('layout_design.gds')