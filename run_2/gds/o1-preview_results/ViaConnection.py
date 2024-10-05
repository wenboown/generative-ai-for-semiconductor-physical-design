import gdspy

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MYLAYOUT')

# Layer definitions
VIA_LAYER = 1    # Yellow
METAL_LAYER = 2  # Blue
PAD_LAYER = 3    # Red

# Parameters
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600

# Positions
via_positions = [(50, 150), (550, 150)]  # Positions of the vias
metal_x0 = 0  # Starting x-position of the metal connection
metal_y0 = 150 - metal_width / 2  # Center the metal vertically around y=150

# Calculate pad positions
pad_margin = 10  # Margin between the edge of the metal and the pads
pad_positions = [
    (metal_x0 - pad_margin - pad_radius, 150),  # Left pad
    (metal_x0 + metal_length + pad_margin + pad_radius, 150)  # Right pad
]

# Create vias (circles on the VIA_LAYER)
for position in via_positions:
    via = gdspy.Round(position, via_radius, layer=VIA_LAYER)
    cell.add(via)

# Create metal connection (rectangle on the METAL_LAYER)
metal = gdspy.Rectangle(
    (metal_x0, metal_y0),
    (metal_x0 + metal_length, metal_y0 + metal_width),
    layer=METAL_LAYER
)
cell.add(metal)

# Create pads (circles on the PAD_LAYER)
for position in pad_positions:
    pad = gdspy.Round(position, pad_radius, layer=PAD_LAYER)
    cell.add(pad)

# Save the GDSII file
lib.write_gds('layout.gds')