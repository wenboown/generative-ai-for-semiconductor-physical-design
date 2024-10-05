import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Define the layers
active_layer = 0
gate_layer = 1
contact_layer = 2

# Draw the active region (10 µm x 5 µm)
active_region = gdspy.Rectangle((0, 0), (10, 5), active_layer)
cell.add(active_region)

# Draw the polysilicon gate (1 µm width, vertical, centered at 5 µm)
gate = gdspy.Rectangle((4.5, 0), (5.5, 5), gate_layer)
cell.add(gate)

# Draw the contact holes (1 µm x 1 µm, 1 µm away from gate on either side)
contact_left = gdspy.Rectangle((3.5, 2), (4.5, 3), contact_layer)
cell.add(contact_left)
contact_right = gdspy.Rectangle((5.5, 2), (6.5, 3), contact_layer)
cell.add(contact_right)

# Save the design to a GDS file
lib.write_gds('layout.gds')