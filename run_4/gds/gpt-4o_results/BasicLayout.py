import gdspy

# Create a library and a cell for the design
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DESIGN')

# Define the dimensions and coordinates
active_width = 10.0
active_height = 5.0
gate_width = 1.0
contact_size = 1.0

# Create the rectangular active region
active_region = gdspy.Rectangle((0, 0), (active_width, active_height))
cell.add(active_region)

# Create the polysilicon gate crossing the active region vertically at its center
gate_x = (active_width - gate_width) / 2
gate_region = gdspy.Rectangle((gate_x, 0), (gate_x + gate_width, active_height))
cell.add(gate_region)

# Create the contact holes
contact1_x = gate_x - contact_size - 1.0
contact2_x = gate_x + gate_width + 1.0
contact1 = gdspy.Rectangle((contact1_x, 2.0), (contact1_x + contact_size, 2.0 + contact_size))
contact2 = gdspy.Rectangle((contact2_x, 2.0), (contact2_x + contact_size, 2.0 + contact_size))

# Add the contact holes to the cell
cell.add(contact1)
cell.add(contact2)

# Save the design to a GDS file
lib.write_gds('output.gds')

print("GDS layout created and saved to 'output.gds'.")