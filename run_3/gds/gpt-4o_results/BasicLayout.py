import gdspy

# Step 1: Create a new GDSII library
lib = gdspy.GdsLibrary()

# Step 2: Create a cell that will contain the layout design
cell = lib.new_cell('ACTIVE_REGION_DESIGN')

# Step 3: Define the rectangular active region
active_width = 10.0  # in micrometers
active_height = 5.0  # in micrometers
active_x0 = 0.0
active_y0 = 0.0
active_region = gdspy.Rectangle(
    (active_x0, active_y0), (active_x0 + active_width, active_y0 + active_height)
)

# Add the active region to the cell
cell.add(active_region)

# Step 4: Define the polysilicon gate
gate_width = 1.0  # in micrometers
gate_height = active_height  # same height as the active region
gate_x0 = active_x0 + (active_width - gate_width) / 2.0
gate_y0 = active_y0
polysilicon_gate = gdspy.Rectangle(
    (gate_x0, gate_y0), (gate_x0 + gate_width, gate_y0 + gate_height)
)

# Add the polysilicon gate to the cell
cell.add(polysilicon_gate)

# Step 5: Define the square contact holes
contact_width = 1.0  # in micrometers
contact_height = 1.0  # in micrometers
contact_spacing = 1.0  # distance from gate

# Left contact hole
left_contact_x0 = gate_x0 - contact_spacing - contact_width
left_contact_y0 = gate_y0 + (active_height - contact_height) / 2
left_contact = gdspy.Rectangle(
    (left_contact_x0, left_contact_y0), (left_contact_x0 + contact_width, left_contact_y0 + contact_height)
)

# Right contact hole
right_contact_x0 = gate_x0 + gate_width + contact_spacing
right_contact_y0 = gate_y0 + (active_height - contact_height) / 2
right_contact = gdspy.Rectangle(
    (right_contact_x0, right_contact_y0), (right_contact_x0 + contact_width, right_contact_y0 + contact_height)
)

# Add the contact holes to the cell
cell.add(left_contact)
cell.add(right_contact)

# Step 6: Save the design to a GDS file
gdspy.write_gds('active_region_design.gds', [cell])

print("GDS file written: 'active_region_design.gds'")