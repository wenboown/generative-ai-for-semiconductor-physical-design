import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TOP')

# Define layers
via_layer = 1    # Via layer (yellow)
metal_layer = 2  # Metal layer (blue)
pad_layer = 3    # Pad layer (red)

# Define via parameters
via_radius = 10
via_positions = [(50, 150), (550, 150)]

# Create vias on the via layer
for position in via_positions:
    via = gdspy.Round(position, via_radius, number_of_points=64, layer=via_layer)
    cell.add(via)

# Define pad parameters
pad_radius = 30

# Create pads on the pad layer
for position in via_positions:
    pad = gdspy.Round(position, pad_radius, number_of_points=64, layer=pad_layer)
    cell.add(pad)

# Define metal connection parameters
metal_width = 40    # Vertical width (height) of the metal connection
metal_length = 600  # Total length of the metal connection

# Calculate coordinates for the metal connection
metal_x_start = 0
metal_x_end = metal_length
metal_y_center = 150
metal_y_start = metal_y_center - metal_width / 2
metal_y_end = metal_y_center + metal_width / 2

# Create the metal connection rectangle on the metal layer
metal_connection = gdspy.Rectangle(
    (metal_x_start, metal_y_start),
    (metal_x_end, metal_y_end),
    layer=metal_layer
)
cell.add(metal_connection)

# Save the design to a GDS file
lib.write_gds('design.gds')