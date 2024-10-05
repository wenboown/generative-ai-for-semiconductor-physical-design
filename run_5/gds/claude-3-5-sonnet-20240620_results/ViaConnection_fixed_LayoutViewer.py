import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# Define layer numbers
VIA_LAYER = 1
METAL_LAYER = 2
PAD_LAYER = 3

# Define dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
total_length = 600
via1_pos = (50, 150)
via2_pos = (550, 150)

# Create vias
via1 = gdspy.Round(via1_pos, via_radius, layer=VIA_LAYER)
via2 = gdspy.Round(via2_pos, via_radius, layer=VIA_LAYER)

# Create pads
pad1 = gdspy.Round(via1_pos, pad_radius, layer=PAD_LAYER)
pad2 = gdspy.Round(via2_pos, pad_radius, layer=PAD_LAYER)

# Create metal connection
metal_start_x = via1_pos[0] - 50
metal_end_x = via2_pos[0] + 50
metal_y = via1_pos[1]

metal = gdspy.Rectangle((metal_start_x, metal_y - metal_width/2),
                        (metal_end_x, metal_y + metal_width/2),
                        layer=METAL_LAYER)

# Add all elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(pad1)
cell.add(pad2)
cell.add(metal)

# Save the design to a GDS file
lib.write_gds('three_layer_design.gds')

# Optional: View the layout