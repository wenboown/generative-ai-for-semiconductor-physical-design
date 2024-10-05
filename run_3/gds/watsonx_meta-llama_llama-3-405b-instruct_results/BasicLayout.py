import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Define the active region (10 µm x 5 µm rectangle)
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1, datatype=0)
cell.add(active_region)

# Calculate the center of the active region
center_x = 5
center_y = 2.5

# Define the polysilicon gate (1 µm wide, crossing the active region vertically at its center)
gate = gdspy.Rectangle((center_x - 0.5, 0), (center_x + 0.5, 5), layer=2, datatype=0)
cell.add(gate)

# Define the two square contact holes (1 µm x 1 µm, positioned 1 µm away from the gate on either side)
contact_hole1 = gdspy.Rectangle((center_x - 1.5, center_y - 0.5), (center_x - 0.5, center_y + 0.5), layer=3, datatype=0)
contact_hole2 = gdspy.Rectangle((center_x + 0.5, center_y - 0.5), (center_x + 1.5, center_y + 0.5), layer=3, datatype=0)
cell.add(contact_hole1)
cell.add(contact_hole2)

# Save the design to a GDS file
lib.write_gds('layout.gds')