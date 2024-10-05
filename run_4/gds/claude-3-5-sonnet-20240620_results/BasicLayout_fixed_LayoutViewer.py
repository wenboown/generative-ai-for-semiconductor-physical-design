import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MOSFET')

# 1. Create the active region (10 µm x 5 µm)
active = gdspy.Rectangle((0, 0), (10, 5))
cell.add(active)

# 2. Create the polysilicon gate (1 µm wide, centered)
gate_width = 1
gate_x = 5 - gate_width / 2
gate = gdspy.Rectangle((gate_x, -1), (gate_x + gate_width, 6))
cell.add(gate)

# 3. Create two contact holes (1 µm x 1 µm, 1 µm away from the gate on each side)
contact_size = 1
contact_spacing = 1

# Left contact
left_contact_x = gate_x - contact_spacing - contact_size
left_contact = gdspy.Rectangle((left_contact_x, 2), (left_contact_x + contact_size, 3))
cell.add(left_contact)

# Right contact
right_contact_x = gate_x + gate_width + contact_spacing
right_contact = gdspy.Rectangle((right_contact_x, 2), (right_contact_x + contact_size, 3))
cell.add(right_contact)

# Save the layout to a GDSII file
lib.write_gds('mosfet_layout.gds')

# Optional: View the layout