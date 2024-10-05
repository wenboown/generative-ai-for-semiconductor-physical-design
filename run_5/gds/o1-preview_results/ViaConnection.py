import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('MY_LAYOUT')

# Define layer numbers for the different layers
VIA_LAYER = 1    # Yellow
METAL_LAYER = 2  # Blue
PAD_LAYER = 3    # Red

# Define properties for vias
via_radius = 10
via_positions = [(50, 150), (550, 150)]

# Create vias and add them to the cell
for position in via_positions:
    via = gdspy.Round(
        center=position,
        radius=via_radius,
        number_of_points=64,
        layer=VIA_LAYER
    )
    cell.add(via)

# Define properties for pads
pad_radius = 30
pad_positions = [(50, 150), (550, 150)]

# Create pads and add them to the cell
for position in pad_positions:
    pad = gdspy.Round(
        center=position,
        radius=pad_radius,
        number_of_points=64,
        layer=PAD_LAYER
    )
    cell.add(pad)

# Define properties for the metal connection
metal_width = 40
metal_length = 600
metal_left = 0  # x-coordinate of the left edge
metal_right = metal_left + metal_length  # x-coordinate of the right edge
metal_bottom = 150 - (metal_width / 2)  # y-coordinate of the bottom edge
metal_top = 150 + (metal_width / 2)     # y-coordinate of the top edge

# Create the metal connection rectangle and add it to the cell
metal_connection = gdspy.Rectangle(
    (metal_left, metal_bottom),
    (metal_right, metal_top),
    layer=METAL_LAYER
)
cell.add(metal_connection)

# Save the layout to a GDSII file
lib.write_gds('layout.gds')