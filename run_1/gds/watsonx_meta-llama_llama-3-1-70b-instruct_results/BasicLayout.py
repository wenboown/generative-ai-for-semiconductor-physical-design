import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Layout")

# Define the rectangular active region with dimensions 10 µm x 5 µm
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(active_region)

# Define the polysilicon gate with a width of 1 µm, crossing the active region vertically at its center
gate_width = 1
gate_length = 5
gate_center_x = 5
gate_center_y = 2.5
gate = gdspy.Rectangle((gate_center_x - gate_width / 2, 0), (gate_center_x + gate_width / 2, gate_length), layer=2)
cell.add(gate)

# Add two square contact holes, each 1 µm x 1 µm, positioned 1 µm away from the gate on either side along the active region
contact_size = 1
contact_spacing = 1
contact-hole1 = gdspy.Rectangle((gate_center_x - gate_width / 2 - contact_spacing - contact_size, 2), (gate_center_x - gate_width / 2 - contact_spacing, 3), layer=3)
contact-hole2 = gdspy.Rectangle((gate_center_x + gate_width / 2 + contact_spacing, 2), (gate_center_x + gate_width / 2 + contact_spacing + contact_size, 3), layer=3)
cell.add(contact-hole1)
cell.add(contact-hole2)

# Save the design to a GDS file
lib.write_gds("layout.gds")