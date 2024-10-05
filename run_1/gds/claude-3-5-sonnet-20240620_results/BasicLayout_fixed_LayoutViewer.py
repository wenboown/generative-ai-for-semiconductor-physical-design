import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MOSFET')

# 1. Draw the active region (10 µm x 5 µm)
active = gdspy.Rectangle((0, 0), (10, 5))
cell.add(active)

# 2. Place the polysilicon gate (1 µm wide, centered vertically)
gate_width = 1
gate_x = 5  # Centered horizontally
gate = gdspy.Rectangle((gate_x - gate_width/2, -1), (gate_x + gate_width/2, 6))
cell.add(gate)

# 3. Add two square contact holes (1 µm x 1 µm), 1 µm away from the gate on either side
contact_size = 1
contact_spacing = 1

# Left contact
left_contact = gdspy.Rectangle(
    (gate_x - gate_width/2 - contact_spacing - contact_size, 2),
    (gate_x - gate_width/2 - contact_spacing, 3)
)
cell.add(left_contact)

# Right contact
right_contact = gdspy.Rectangle(
    (gate_x + gate_width/2 + contact_spacing, 2),
    (gate_x + gate_width/2 + contact_spacing + contact_size, 3)
)
cell.add(right_contact)

# Save the layout to a GDS file
lib.write_gds('mosfet_layout.gds')

# Optionally, view the layout