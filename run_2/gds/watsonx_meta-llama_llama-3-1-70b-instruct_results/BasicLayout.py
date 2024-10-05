import gdspy

# Step 1: Create a new library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Layout')

# Step 2: Define the active region
active_region = gdspy.Rectangle((0, 0), (10, 5))

# Step 3: Create the polysilicon gate
gate_width = 1
gate_center_x = 5  # Center of the active region
gate = gdspy.Rectangle((gate_center_x - gate_width/2, 0), (gate_center_x + gate_width/2, 5))

# Step 4: Add contact holes
contact_size = 1
contact.spacing = 1
contact1 = gdspy.Rectangle((gate_center_x - gate_width/2 - contact_size - contact_spacing, 1), (gate_center_x - gate_width/2 - contact_spacing, 2))
contact2 = gdspy.Rectangle((gate_center_x + gate_width/2 + contact_spacing, 1), (gate_center_x + gate_width/2 + contact_size + contact_spacing, 2))

# Step 5: Add elements to the cell
cell.add(active_region)
cell.add(gate)
cell.add(contact1)
cell.add(contact2)

# Step 6: Save the design to a GDS file
lib.write_gds('layout.gds')