import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('METAL_VIA_PAD')

# Define layers
VIA_LAYER = 1
METAL_LAYER = 2
PAD_LAYER = 3

# Define dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
total_length = 600
via1_x, via1_y = 50, 150
via2_x, via2_y = 550, 150

# Calculate metal connection coordinates
metal_start_x = via1_x - 50
metal_end_x = via2_x + 50
metal_y = via1_y

# Create vias
via1 = gdspy.Round((via1_x, via1_y), via_radius, layer=VIA_LAYER)
via2 = gdspy.Round((via2_x, via2_y), via_radius, layer=VIA_LAYER)

# Create metal connection
metal = gdspy.Rectangle(
    (metal_start_x, metal_y - metal_width/2),
    (metal_end_x, metal_y + metal_width/2),
    layer=METAL_LAYER
)

# Create pads
pad1 = gdspy.Round((via1_x, via1_y), pad_radius, layer=PAD_LAYER)
pad2 = gdspy.Round((via2_x, via2_y), pad_radius, layer=PAD_LAYER)

# Add all elements to the cell
cell.add(via1)
cell.add(via2)
cell.add(metal)
cell.add(pad1)
cell.add(pad2)

# Save the design to a GDS file
lib.write_gds('metal_via_pad_design.gds')

# Optional: View the layout