import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the layout
cell = lib.new_cell('MYLAYOUT')

# Layer definitions
VIA_LAYER = 1    # Via layer (yellow)
METAL_LAYER = 2  # Metal layer (blue)
PAD_LAYER = 3    # Pad layer (red)

# Define positions
via_positions = [(50, 150), (550, 150)]
pad_positions = [(50, 150), (550, 150)]

# Define dimensions
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600

# Calculate pad edges for margin calculation
pad_left_edge = 20    # 50 (pad center) - 30 (pad radius)
pad_right_edge = 580  # 550 (pad center) + 30 (pad radius)

# Metal connection extends from x = 30 to x = 570 to leave a 10-unit margin to pads
metal_x_start = pad_left_edge + 10  # 20 + 10 = 30
metal_x_end = pad_right_edge - 10   # 580 - 10 = 570
metal_length_actual = metal_x_end - metal_x_start  # 570 - 30 = 540

# Metal connection (rectangle)
metal = gdspy.Rectangle(
    (metal_x_start, 150 - metal_width / 2),
    (metal_x_end, 150 + metal_width / 2),
    layer=METAL_LAYER
)
cell.add(metal)

# Create vias (circles)
for position in via_positions:
    via = gdspy.Round(
        position,
        via_radius,
        number_of_points=64,
        layer=VIA_LAYER
    )
    cell.add(via)

# Create pads (circles)
for position in pad_positions:
    pad = gdspy.Round(
        position,
        pad_radius,
        number_of_points=64,
        layer=PAD_LAYER
    )
    cell.add(pad)

# Write the GDSII file
lib.write_gds('layout.gds')