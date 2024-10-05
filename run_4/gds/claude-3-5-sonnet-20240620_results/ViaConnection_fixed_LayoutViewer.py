import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('VIA_METAL_PAD')

# Define layers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Define dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
metal_margin = 10
via_spacing = 50

# Calculate positions
via1_center = (50, 150)
via2_center = (550, 150)
metal_start = (via1_center[0] - via_spacing, via1_center[1] - metal_width/2)
metal_end = (via2_center[0] + via_spacing, via1_center[1] + metal_width/2)

# Create vias
via1 = gdspy.Round(via1_center, via_radius, layer=via_layer)
via2 = gdspy.Round(via2_center, via_radius, layer=via_layer)

# Create metal connection
metal = gdspy.Rectangle(metal_start, metal_end, layer=metal_layer)

# Create pads
pad1_center = (via1_center[0], via1_center[1])
pad2_center = (via2_center[0], via2_center[1])
pad1 = gdspy.Round(pad1_center, pad_radius, layer=pad_layer)
pad2 = gdspy.Round(pad2_center, pad_radius, layer=pad_layer)

# Add all elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(metal)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('via_metal_pad_design.gds')

# Optional: View the layout