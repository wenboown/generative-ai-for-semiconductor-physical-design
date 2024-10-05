import gdspy

# Parse user's design specifications
active_region_size = (10, 5)  # µm
gate_width = 1  # µm
contact_hole_size = (1, 1)  # µm
contact_hole_spacing = 1  # µm

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('layout')

# Create rectangular active region
active_region = gdspy.Rectangle(
    (0, 0), (active_region_size[0], active_region_size[1]),
    layer=1  # Layer 1 for active region
)
cell.add(active_region)

# Create polysilicon gate
gate = gdspy.Rectangle(
    (active_region_size[0] / 2 - gate_width / 2, 0),
    (active_region_size[0] / 2 + gate_width / 2, active_region_size[1]),
    layer=2  # Layer 2 for polysilicon gate
)
cell.add(gate)

# Create square contact holes
contact_hole_left = gdspy.Rectangle(
    (gate.x - gate_width / 2 - contact_hole_size[0] - contact_hole_spacing, 0),
    (gate.x - gate_width / 2 - contact_hole_spacing, contact_hole_size[1]),
    layer=3  # Layer 3 for contact holes
)
cell.add(contact_hole_left)

contact_hole_right = gdspy.Rectangle(
    (gate.x + gate_width / 2 + contact_hole_spacing, 0),
    (gate.x + gate_width / 2 + contact_hole_size[0] + contact_hole_spacing, contact_hole_size[1]),
    layer=3  # Layer 3 for contact holes
)
cell.add(contact_hole_right)

# Save the design to a GDS file
lib.write_gds('layout.gds')