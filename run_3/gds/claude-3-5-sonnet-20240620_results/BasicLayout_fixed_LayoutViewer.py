import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MOSFET')

# 1. Create the active region (10 µm x 5 µm)
active = gdspy.Rectangle((-5, -2.5), (5, 2.5), layer=1)
cell.add(active)

# 2. Create the polysilicon gate (1 µm wide, centered)
gate = gdspy.Rectangle((-0.5, -2.5), (0.5, 2.5), layer=2)
cell.add(gate)

# 3. Create two contact holes (1 µm x 1 µm each)
contact_left = gdspy.Rectangle((-2.5, -0.5), (-1.5, 0.5), layer=3)
contact_right = gdspy.Rectangle((1.5, -0.5), (2.5, 0.5), layer=3)
cell.add(contact_left)
cell.add(contact_right)

# Save the layout to a GDSII file
lib.write_gds('mosfet_layout.gds')

# Display all cells using the internal viewer