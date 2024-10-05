import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the main cell
cell = lib.new_cell('LAYOUT')

# Geometric properties
via_radius = 10
pad_radius = 30
metal_width = 40
total_length = 600
space_from_via_to_edge = 50
margin = 10  # Additional margin between metal and pad as specified

# Layers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Via and pad positions
via1_center = (50, 150)
via2_center = (550, 150)

# Create vias
via1 = gdspy.Round(via1_center, via_radius, layer=via_layer)
via2 = gdspy.Round(via2_center, via_radius, layer=via_layer)

# Create pads
pad1 = gdspy.Round(via1_center, pad_radius, layer=pad_layer)
pad2 = gdspy.Round(via2_center, pad_radius, layer=pad_layer)

# Metal connection coordinates
metal_x1 = via1_center[0] - space_from_via_to_edge
metal_x2 = via2_center[0] + space_from_via_to_edge
metal_y1 = via1_center[1] - metal_width / 2
metal_y2 = via1_center[1] + metal_width / 2

# Create metal connection
metal = gdspy.Rectangle((metal_x1, metal_y1), (metal_x2, metal_y2), layer=metal_layer)

# Add shapes to cell
cell.add([via1, via2, pad1, pad2, metal])

# Save to GDS file
lib.write_gds('layout_design.gds')