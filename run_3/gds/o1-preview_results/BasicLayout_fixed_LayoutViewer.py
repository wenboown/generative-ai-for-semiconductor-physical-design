import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MYCELL')

# Dimensions in micrometers
# Active region dimensions
active_width = 10.0  # µm
active_height = 5.0   # µm

# Polysilicon gate dimensions
gate_width = 1.0      # µm
gate_height = active_height  # µm

# Contact hole dimensions
contact_size = 1.0    # µm (square)
contact_spacing = 1.0 # µm (spacing from gate)

# Calculate positions
# Active region coordinates
active_origin = (0, 0)
active_destination = (active_width, active_height)

# Polysilicon gate coordinates (centered)
gate_x = (active_width - gate_width) / 2
gate_origin = (gate_x, 0)
gate_destination = (gate_x + gate_width, gate_height)

# Left contact coordinates
left_contact_x = gate_x - contact_spacing - contact_size
left_contact_y = (active_height - contact_size) / 2
left_contact_origin = (left_contact_x, left_contact_y)
left_contact_destination = (left_contact_x + contact_size, left_contact_y + contact_size)

# Right contact coordinates
right_contact_x = gate_x + gate_width + contact_spacing
right_contact_y = left_contact_y
right_contact_origin = (right_contact_x, right_contact_y)
right_contact_destination = (right_contact_x + contact_size, right_contact_y + contact_size)

# Create the active region rectangle on layer 1
active_region = gdspy.Rectangle(
    active_origin,
    active_destination,
    layer=1
)
cell.add(active_region)

# Create the polysilicon gate rectangle on layer 2
polysilicon_gate = gdspy.Rectangle(
    gate_origin,
    gate_destination,
    layer=2
)
cell.add(polysilicon_gate)

# Create the left contact hole rectangle on layer 3
left_contact = gdspy.Rectangle(
    left_contact_origin,
    left_contact_destination,
    layer=3
)
cell.add(left_contact)

# Create the right contact hole rectangle on layer 3
right_contact = gdspy.Rectangle(
    right_contact_origin,
    right_contact_destination,
    layer=3
)
cell.add(right_contact)

# Save the GDSII file
lib.write_gds('layout.gds')

# Optional: View the layout