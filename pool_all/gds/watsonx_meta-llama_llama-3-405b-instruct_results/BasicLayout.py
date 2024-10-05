import gdspy

# Define the dimensions and layers
active_width = 10.0
active_height = 5.0
gate_width = 1.0
contact_size = 1.0
contact_spacing = 1.0
active_layer = 1
gate_layer = 2
contact_layer = 3

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MOSFET_LAYOUT')

# Create the active region
active_region = gdspy.Rectangle((0, 0), (active_width, active_height), layer=active_layer)
cell.add(active_region)

# Calculate the center of the active region
active_center_x = active_width / 2

# Create the polysilicon gate
gate = gdspy.Rectangle((active_center_x - gate_width / 2, 0), (active_center_x + gate_width / 2, active_height), layer=gate_layer)
cell.add(gate)

# Create the contact holes
contact_1_x = active_center_x - gate_width / 2 - contact_spacing - contact_size
contact_2_x = active_center_x + gate_width / 2 + contact_spacing
contact_1 = gdspy.Rectangle((contact_1_x, (active_height - contact_size) / 2), (contact_1_x + contact_size, (active_height + contact_size) / 2), layer=contact_layer)
contact_2 = gdspy.Rectangle((contact_2_x, (active_height - contact_size) / 2), (contact_2_x + contact_size, (active_height + contact_size) / 2), layer=contact_layer)
cell.add(contact_1)
cell.add(contact_2)

# Save the design to a GDS file
lib.write_gds('mosfet_layout.gds')