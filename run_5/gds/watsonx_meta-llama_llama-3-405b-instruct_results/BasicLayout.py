import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layers
active_layer = 1
gate_layer = 2
contact_layer = 3

# Draw the rectangular active region
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=active_layer)
cell.add(active_region)

# Calculate the gate position to be at the center of the active region
gate_x = 5
gate_y = 0
gate_height = 5

# Draw the polysilicon gate
gate = gdspy.Rectangle((gate_x - 0.5, gate_y), (gate_x + 0.5, gate_y + gate_height), layer=gate_layer)
cell.add(gate)

# Calculate the contact hole positions to be 1 µm away from the gate on either side
contact_x1 = gate_x - 1.5
contact_x2 = gate_x + 1.5
contact_y = gate_y + gate_height / 2 - 0.5

# Draw the square contact holes
contact1 = gdspy.Rectangle((contact_x1, contact_y), (contact_x1 + 1, contact_y + 1), layer=contact_layer)
contact2 = gdspy.Rectangle((contact_x2, contact_y), (contact_x2 + 1, contact_y + 1), layer=contact_layer)
cell.add(contact1)
cell.add(contact2)

# Save the design to a GDS file
lib.write_gds('design.gds')