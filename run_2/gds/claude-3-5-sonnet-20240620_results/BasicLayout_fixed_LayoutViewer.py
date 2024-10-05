import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MOSFET')

# 1. Create the active region (10 µm x 5 µm)
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(active_region)

# 2. Create the polysilicon gate (1 µm wide, centered vertically)
gate_width = 1
gate_x_position = 5  # Center of the active region
gate = gdspy.Rectangle((gate_x_position - gate_width/2, -1), (gate_x_position + gate_width/2, 6), layer=2)
cell.add(gate)

# 3. Add two square contact holes (1 µm x 1 µm)
contact_size = 1
contact_spacing = 1

# Left contact
left_contact_x = gate_x_position - gate_width/2 - contact_spacing - contact_size
left_contact = gdspy.Rectangle((left_contact_x, 2), (left_contact_x + contact_size, 3), layer=3)
cell.add(left_contact)

# Right contact
right_contact_x = gate_x_position + gate_width/2 + contact_spacing
right_contact = gdspy.Rectangle((right_contact_x, 2), (right_contact_x + contact_size, 3), layer=3)
cell.add(right_contact)

# Save the layout to a GDS file
lib.write_gds('mosfet_layout.gds')

# Optional: View the layout