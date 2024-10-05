import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('Layout')

# Define layers
active_layer = 1
gate_layer = 2
contact_layer = 3

# 1. Draw the active region (10 µm x 5 µm)
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=active_layer)
cell.add(active_region)

# 2. Place the polysilicon gate (1 µm wide, vertically centered at 5 µm)
gate_x_center = 5
gate_width = 1
gate = gdspy.Rectangle((gate_x_center - gate_width/2, 0), (gate_x_center + gate_width/2, 5), layer=gate_layer)
cell.add(gate)

# 3. Define two square contact holes (1 µm x 1 µm) positioned 1 µm from the gate
contact_size = 1
contact_spacing = 1

# Left contact
contact_left_x = gate_x_center - gate_width/2 - contact_spacing - contact_size
contact_left = gdspy.Rectangle((contact_left_x, 2), (contact_left_x + contact_size, 3), layer=contact_layer)
cell.add(contact_left)

# Right contact
contact_right_x = gate_x_center + gate_width/2 + contact_spacing
contact_right = gdspy.Rectangle((contact_right_x, 2), (contact_right_x + contact_size, 3), layer=contact_layer)
cell.add(contact_right)

# Save the layout to a GDS file
lib.write_gds('layout_design.gds')