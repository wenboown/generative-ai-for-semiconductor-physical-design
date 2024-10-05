import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('LAYOUT')

# Define layers
VIA_LAYER = 1
METAL_LAYER = 2
PAD_LAYER = 3

# Define dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
via_spacing = 50

# Calculate positions
via1_center = (50, 150)
via2_center = (550, 150)
metal_start = (via1_center[0] - via_spacing, via1_center[1] - metal_width/2)
metal_end = (via2_center[0] + via_spacing, via1_center[1] + metal_width/2)

# Create vias
via1 = gdspy.Round(via1_center, via_radius, layer=VIA_LAYER)
via2 = gdspy.Round(via2_center, via_radius, layer=VIA_LAYER)

# Create metal connection
metal = gdspy.Rectangle(metal_start, metal_end, layer=METAL_LAYER)

# Create pads
pad1 = gdspy.Round(via1_center, pad_radius, layer=PAD_LAYER)
pad2 = gdspy.Round(via2_center, pad_radius, layer=PAD_LAYER)

# Add all elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(metal)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('layout_design.gds')