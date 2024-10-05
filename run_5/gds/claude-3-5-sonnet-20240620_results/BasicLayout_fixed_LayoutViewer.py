import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MOSFET')

# Create the active region
active = gdspy.Rectangle((-5, -2.5), (5, 2.5), layer=1)
cell.add(active)

# Create the polysilicon gate
gate = gdspy.Rectangle((-0.5, -3.5), (0.5, 3.5), layer=2)
cell.add(gate)

# Create the contact holes
contact_left = gdspy.Rectangle((-2.5, -0.5), (-1.5, 0.5), layer=3)
contact_right = gdspy.Rectangle((1.5, -0.5), (2.5, 0.5), layer=3)
cell.add(contact_left)
cell.add(contact_right)

# Save the design to a GDS file
lib.write_gds('mosfet_layout.gds')

# Optional: View the layout