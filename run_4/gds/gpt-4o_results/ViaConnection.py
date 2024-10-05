import gdspy

# Create a library
lib = gdspy.GdsLibrary()

# Create the main cell
cell = lib.new_cell('LAYOUT')

# Define layers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Define parameters
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
via_positions = [(50, 150), (550, 150)]
pad_margin = 10
metal_edge_margin = 50

# Draw via circles
for via_pos in via_positions:
    via = gdspy.Round(via_pos, via_radius, layer=via_layer)
    cell.add(via)

# Calculate start and end points for the metal connection
metal_start_x = via_positions[0][0] + via_radius + metal_edge_margin
metal_end_x = via_positions[1][0] - via_radius - metal_edge_margin
metal_y = 150

# Draw the metal connection rectangle
metal_rect = gdspy.Rectangle(
    (metal_start_x, metal_y - metal_width / 2),
    (metal_end_x, metal_y + metal_width / 2),
    layer=metal_layer
)
cell.add(metal_rect)

# Calculate pad positions offset by pad_margin
pad_positions = [
    (via_positions[0][0], via_positions[0][1] + pad_margin + pad_radius),
    (via_positions[1][0], via_positions[1][1] + pad_margin + pad_radius)
]

# Draw pad circles
for pad_pos in pad_positions:
    pad = gdspy.Round(pad_pos, pad_radius, layer=pad_layer)
    cell.add(pad)

# Save the design to a GDSII file
lib.write_gds('layout_design_with_layers.gds')