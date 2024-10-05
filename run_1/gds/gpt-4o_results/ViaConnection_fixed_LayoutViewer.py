import gdspy

# Create a new GDSII library for the design
lib = gdspy.GdsLibrary()

# Add a new cell to the library for the layout
cell = lib.new_cell('MY_LAYOUT')

# Constants and parameters
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600

# Position of vias
via1_pos = (50, 150)
via2_pos = (550, 150)

# Compute positions and sizes
pad_margin = 10
metal_margin = 50

# Metal connection coordinates
metal_left = via1_pos[0]
metal_right = via2_pos[0]
metal_top = via1_pos[1] + metal_width / 2
metal_bottom = via1_pos[1] - metal_width / 2

# Create vias
via1 = gdspy.Round(via1_pos, via_radius, layer=1)  # via layer, e.g., yellow (layer 1)
via2 = gdspy.Round(via2_pos, via_radius, layer=1)  # via layer, e.g., yellow (layer 1)
cell.add(via1)
cell.add(via2)

# Create connections using metal layer
metal_connection = gdspy.Rectangle(
    (metal_left - metal_margin, metal_bottom),
    (metal_right + metal_margin, metal_top),
    layer=2  # metal layer, e.g., blue (layer 2)
)
cell.add(metal_connection)

# Create pads
pad1 = gdspy.Round(via1_pos, pad_radius, layer=3)  # pad layer, e.g., red (layer 3)
pad2 = gdspy.Round(via2_pos, pad_radius, layer=3)  # pad layer, e.g., red (layer 3)
cell.add(pad1)
cell.add(pad2)

# Output the GDS file
gdspy.write_gds('layout_design.gds', [cell])

# Viewing the result with an optional built-in viewer