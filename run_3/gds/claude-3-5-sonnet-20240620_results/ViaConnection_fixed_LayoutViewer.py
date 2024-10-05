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
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
via_x_positions = [50, 550]
via_y_position = 150

# Create metal connection
metal = gdspy.Rectangle((50, 130), (550, 170), layer=METAL_LAYER)
cell.add(metal)

# Create vias and pads
for x in via_x_positions:
    # Via
    via = gdspy.Round((x, via_y_position), via_radius, layer=VIA_LAYER)
    cell.add(via)
    
    # Pad
    pad = gdspy.Round((x, via_y_position), pad_radius, layer=PAD_LAYER)
    cell.add(pad)

# Save the design to a GDS file
lib.write_gds('design.gds')

# Optional: View the layout