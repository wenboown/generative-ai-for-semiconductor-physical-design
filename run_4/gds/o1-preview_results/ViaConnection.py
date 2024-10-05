import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MY_CELL')

# Define layers
via_layer = 1     # Via layer (yellow)
metal_layer = 2   # Metal layer (blue)
pad_layer = 3     # Pad layer (red)

# Design parameters
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
via_positions = [(50, 150), (550, 150)]
space_between_vias_and_metal_edge = 50
metal_margin_to_pads = 10

# Calculate metal connection start and end positions
metal_start_x = via_positions[0][0] - space_between_vias_and_metal_edge
metal_end_x = via_positions[1][0] + space_between_vias_and_metal_edge

# Adjust metal length if necessary
actual_metal_length = metal_end_x - metal_start_x
if actual_metal_length != metal_length:
    # Adjust the metal_end_x to match the total metal_length
    metal_end_x = metal_start_x + metal_length

# Metal connection rectangle (ensuring it fully covers the vias and leaves margin to pads)
metal_connection = gdspy.Rectangle(
    (metal_start_x, via_positions[0][1] - metal_width / 2),
    (metal_end_x, via_positions[0][1] + metal_width / 2),
    layer=metal_layer
)

# Add metal connection to the cell
cell.add(metal_connection)

# Create vias and pads
for position in via_positions:
    # Via
    via = gdspy.Round(
        center=position,
        radius=via_radius,
        number_of_points=64,
        layer=via_layer
    )
    cell.add(via)

    # Pad
    pad = gdspy.Round(
        center=position,
        radius=pad_radius,
        number_of_points=64,
        layer=pad_layer
    )
    cell.add(pad)

# Calculate pad edges for margin adjustments
for position in via_positions:
    pad_x_min = position[0] - pad_radius
    pad_x_max = position[0] + pad_radius

    # Left edge of metal connection
    if metal_start_x < pad_x_min - metal_margin_to_pads:
        metal_start_adjusted = metal_start_x
    else:
        metal_start_adjusted = pad_x_min - metal_margin_to_pads

    # Right edge of metal connection
    if metal_end_x > pad_x_max + metal_margin_to_pads:
        metal_end_adjusted = metal_end_x
    else:
        metal_end_adjusted = pad_x_max + metal_margin_to_pads

    # Update metal connection to ensure margin to pads
    metal_connection = gdspy.Rectangle(
        (metal_start_adjusted, position[1] - metal_width / 2),
        (metal_end_adjusted, position[1] + metal_width / 2),
        layer=metal_layer
    )
    cell.add(metal_connection)

# Save the GDSII file
lib.write_gds('design.gds')