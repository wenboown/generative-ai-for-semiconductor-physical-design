import gdspy

# Create a new GDSII library, which will contain the design
lib = gdspy.GdsLibrary()

# Create a new cell ("top" level cell)
cell = lib.new_cell('CELL')

# 1. Draw a rectangular active region with dimensions 10 µm x 5 µm.
# Assuming lower-left corner at (0, 0)
active_width = 10.0  # µm
active_height = 5.0  # µm
active_region = gdspy.Rectangle(
    (0, 0), (active_width, active_height), layer=1
)
cell.add(active_region)

# 2. Place a polysilicon gate that crosses the active region vertically at its center, with a width of 1 µm.
gate_width = 1.0  # µm
gate_x0 = (active_width - gate_width) / 2
gate_x1 = gate_x0 + gate_width
gate_y0 = 0
gate_y1 = active_height
polysilicon_gate = gdspy.Rectangle(
    (gate_x0, gate_y0), (gate_x1, gate_y1), layer=2
)
cell.add(polysilicon_gate)

# 3. Add two square contact holes, each 1 µm x 1 µm, positioned 1 µm away from the gate on either side along the active region.
contact_size = 1.0  # µm
contact_spacing = 1.0  # µm

# Left contact hole
left_contact_x0 = gate_x0 - contact_spacing - contact_size
left_contact_y0 = (active_height - contact_size) / 2
left_contact = gdspy.Rectangle(
    (left_contact_x0, left_contact_y0),
    (left_contact_x0 + contact_size, left_contact_y0 + contact_size),
    layer=3
)
cell.add(left_contact)

# Right contact hole
right_contact_x0 = gate_x1 + contact_spacing
right_contact_y0 = (active_height - contact_size) / 2
right_contact = gdspy.Rectangle(
    (right_contact_x0, right_contact_y0),
    (right_contact_x0 + contact_size, right_contact_y0 + contact_size),
    layer=3
)
cell.add(right_contact)

# Save the design to a GDSII file
lib.write_gds('layout.gds')