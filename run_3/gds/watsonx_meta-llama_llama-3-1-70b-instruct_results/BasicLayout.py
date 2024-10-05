import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Layout')

# Define the active region (10 µm x 5 µm)
active_region = gdspy.Rectangle(
    (0, 0), 
    (10, 5), 
    layer=1,  # Layer number for the active region
    datatype=0
)
cell.add(active_region)

# Define the polysilicon gate (1 µm wide)
gate_width = 1
gate_height = 5
gate_x = 5 - gate_width/2  # Centered vertically
gate = gdspy.Rectangle(
    (gate_x, 0), 
    (gate_x + gate_width, gate_height), 
    layer=2,  # Layer number for the polysilicon gate
    datatype=0
)
cell.add(gate)

# Define the contact holes (1 µm x 1 µm each)
-contact_width = 1
contact_height = 1
-contact_spacing = 1
contact_left_x = gate_x - contact_spacing - contact_width
contact_right_x = gate_x + gate_width + contact_spacing
contact_top_y = gate_height - contact_height
contact_left = gdspy.Rectangle(
    (contact_left_x, contact_top_y), 
    (contact_left_x + contact_width, contact_top_y + contact_height), 
    layer=3,  # Layer number for the contact holes
    datatype=0
)
cell.add(contact_left)

contact_right = gdspy.Rectangle(
    (contact_right_x, contact_top_y), 
    (contact_right_x + contact_width, contact_top_y + contact_height), 
    layer=3,  # Layer number for the contact holes
    datatype=0
)
cell.add(contact_right)

# Save the design to a GDS file
lib.write_gds('layout.gds')