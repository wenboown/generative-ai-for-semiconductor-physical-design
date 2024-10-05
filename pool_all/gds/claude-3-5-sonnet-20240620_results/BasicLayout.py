import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MOSFET')

# Define layers
LAYER_ACTIVE = 1
LAYER_POLY = 2
LAYER_CONTACT = 3

# Define dimensions (in micrometers)
active_width = 10
active_height = 5
gate_width = 1
contact_size = 1
contact_spacing = 1

# Create the active region
active = gdspy.Rectangle((0, 0), (active_width, active_height), layer=LAYER_ACTIVE)
cell.add(active)

# Create the polysilicon gate
gate_x = active_width / 2 - gate_width / 2
gate = gdspy.Rectangle((gate_x, 0), (gate_x + gate_width, active_height), layer=LAYER_POLY)
cell.add(gate)

# Create the contact holes
contact_y = (active_height - contact_size) / 2
left_contact = gdspy.Rectangle(
    (gate_x - contact_spacing - contact_size, contact_y),
    (gate_x - contact_spacing, contact_y + contact_size),
    layer=LAYER_CONTACT
)
right_contact = gdspy.Rectangle(
    (gate_x + gate_width + contact_spacing, contact_y),
    (gate_x + gate_width + contact_spacing + contact_size, contact_y + contact_size),
    layer=LAYER_CONTACT
)
cell.add(left_contact)
cell.add(right_contact)

# Save the layout to a GDS file
lib.write_gds('mosfet_layout.gds')