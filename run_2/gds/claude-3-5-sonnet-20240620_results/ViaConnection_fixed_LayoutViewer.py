import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DESIGN')

# Define layers
VIA_LAYER = 1
METAL_LAYER = 2
PAD_LAYER = 3

# Define dimensions
VIA_RADIUS = 10
PAD_RADIUS = 30
METAL_WIDTH = 40
TOTAL_LENGTH = 600
VIA_TO_EDGE = 50

# Calculate positions
via1_center = (50, 150)
via2_center = (550, 150)
metal_start = (via1_center[0] - VIA_TO_EDGE, via1_center[1] - METAL_WIDTH / 2)
metal_end = (via2_center[0] + VIA_TO_EDGE, via1_center[1] + METAL_WIDTH / 2)

# Create vias
via1 = gdspy.Round(via1_center, VIA_RADIUS, layer=VIA_LAYER)
via2 = gdspy.Round(via2_center, VIA_RADIUS, layer=VIA_LAYER)

# Create metal connection
metal = gdspy.Rectangle(metal_start, metal_end, layer=METAL_LAYER)

# Create pads
pad1 = gdspy.Round(via1_center, PAD_RADIUS, layer=PAD_LAYER)
pad2 = gdspy.Round(via2_center, PAD_RADIUS, layer=PAD_LAYER)

# Add all shapes to the cell
cell.add(via1)
cell.add(via2)
cell.add(metal)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('design_layout.gds')

# Optional: View the layout