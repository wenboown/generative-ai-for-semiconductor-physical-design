import gdspy

# Units in micrometers (µm), set up basic GDSII library
gdspy.current_library = gdspy.GdsLibrary()
lib = gdspy.current_library
cell = lib.new_cell('MY_LAYOUT')

# Active region dimensions
active_width = 10
active_height = 5
active_layer = 1  # Layer number for active region

# Draw active region rectangle from (0, 0) to (10, 5)
active_region = gdspy.Rectangle((0, 0), (active_width, active_height), layer=active_layer)
cell.add(active_region)

# Polysilicon gate dimensions
gate_width = 1
gate_layer = 2  # Layer number for polysilicon gate

# Gate is centered horizontally at x = 5 µm
gate_x_center = active_width / 2  # 5 µm
gate_left = gate_x_center - gate_width / 2  # 5 - 0.5 = 4.5 µm
gate_right = gate_x_center + gate_width / 2  # 5 + 0.5 = 5.5 µm

# Gate extends along y from 0 to 5 µm (same as active region)
gate = gdspy.Rectangle((gate_left, 0), (gate_right, active_height), layer=gate_layer)
cell.add(gate)

# Contact hole dimensions
contact_size = 1
contact_layer = 3  # Layer number for contact holes

# Positions of contact holes
# Left contact hole center x position
left_contact_center_x = gate_left - 1 - contact_size / 2  # 4.5 - 1 - 0.5 = 3 µm
# Right contact hole center x position
right_contact_center_x = gate_right + 1 + contact_size / 2  # 5.5 + 1 + 0.5 = 7 µm

# Contact holes are centered vertically at y = 2.5 µm
contact_center_y = active_height / 2  # 2.5 µm

# Left contact hole rectangle
left_contact = gdspy.Rectangle(
    (left_contact_center_x - contact_size / 2, contact_center_y - contact_size / 2),
    (left_contact_center_x + contact_size / 2, contact_center_y + contact_size / 2),
    layer=contact_layer)
cell.add(left_contact)

# Right contact hole rectangle
right_contact = gdspy.Rectangle(
    (right_contact_center_x - contact_size / 2, contact_center_y - contact_size / 2),
    (right_contact_center_x + contact_size / 2, contact_center_y + contact_size / 2),
    layer=contact_layer)
cell.add(right_contact)

# Save the GDS file
gdspy.write_gds('layout.gds')