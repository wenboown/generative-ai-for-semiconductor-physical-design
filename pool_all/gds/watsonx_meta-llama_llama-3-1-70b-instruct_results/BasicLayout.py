import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('mosfet_layout')

# Define the active region (10 µm x 5 µm)
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(active_region)

# Define the polysilicon gate (1 µm wide, centered vertically)
gate = gdspy.Rectangle((4.5, 0), (5.5, 5), layer=2)
cell.add(gate)

# Define the contact holes (1 µm x 1 µm, 1 µm away from the gate on either side)
contact_hole_left = gdspy.Rectangle((3.5, 2), (4.5, 3), layer=3)
contact_hole_right = gdspy.Rectangle((5.5, 2), (6.5, 3), layer=3)
cell.add(contact_hole_left)
cell.add(contact_hole_right)

# Save the layout to a GDS file
lib.write_gds('mosfet_layout.gds')