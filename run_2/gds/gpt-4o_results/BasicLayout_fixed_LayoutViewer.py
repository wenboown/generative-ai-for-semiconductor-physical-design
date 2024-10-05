import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Add a new cell to the library
cell = lib.new_cell('LAYOUT')

# 1. Create a rectangular active region with dimensions 10 µm x 5 µm
active_region = gdspy.Rectangle((0, 0), (10, 5))

# 2. Place a polysilicon gate, crossing vertically at the center, with a width of 1 µm
# The vertical center of the active region is at x = 10 µm / 2 = 5 µm
gate = gdspy.Rectangle((4.5, 0), (5.5, 5))

# 3. Add two square contact holes, each 1 µm x 1 µm, positioned 1 µm away from the gate
# Left contact hole: 1 µm away from the left side of the gate
contact_hole_left = gdspy.Rectangle((3.5, 2), (4.5, 3))

# Right contact hole: 1 µm away from the right side of the gate
contact_hole_right = gdspy.Rectangle((5.5, 2), (6.5, 3))

# Add all defined elements to the cell
cell.add(active_region)
cell.add(gate)
cell.add(contact_hole_left)
cell.add(contact_hole_right)

# Save the layout to a GDS file
lib.write_gds('layout_design.gds')

# Optionally, you can use the gdspy library to view the layout