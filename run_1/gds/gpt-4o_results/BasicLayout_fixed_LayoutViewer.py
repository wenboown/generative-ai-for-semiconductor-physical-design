import gdspy

# Constants for dimensions in micrometers.
active_width = 10.0
active_height = 5.0
gate_width = 1.0
contact_size = 1.0
contact_spacing = 1.0

# Create a new GDSII library.
lib = gdspy.GdsLibrary()

# Create a new cell.
cell = lib.new_cell('ACTIVE_REGION_CELL')

# Define the active region as a rectangle.
active_region = gdspy.Rectangle((0, 0), (active_width, active_height), layer=1)

# Calculate the x-position of the center of the active region.
active_center_x = active_width / 2

# Define the polysilicon gate as a rectangle.
gate = gdspy.Rectangle((active_center_x - gate_width / 2, 0), 
                       (active_center_x + gate_width / 2, active_height), 
                       layer=2)

# Define the positions for the contact holes.
contact_1_x = active_center_x - gate_width / 2 - contact_spacing - contact_size
contact_2_x = active_center_x + gate_width / 2 + contact_spacing

contact_1 = gdspy.Rectangle((contact_1_x, (active_height - contact_size) / 2),
                            (contact_1_x + contact_size, (active_height + contact_size) / 2), 
                            layer=3)
contact_2 = gdspy.Rectangle((contact_2_x, (active_height - contact_size) / 2),
                            (contact_2_x + contact_size, (active_height + contact_size) / 2), 
                            layer=3)

# Add all elements to the cell.
cell.add([active_region, gate, contact_1, contact_2])

# Save the library in a GDSII file.
lib.write_gds('layout_design.gds')

# View the layout using gdspy's internal viewer.