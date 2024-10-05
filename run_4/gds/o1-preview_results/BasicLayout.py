import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the layout
cell = lib.new_cell('MY_LAYOUT')

# 1. Draw a rectangular active region with dimensions 10 µm x 5 µm
# Active region from (0, 0) to (10, 5) on layer 1
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(active_region)

# 2. Place a polysilicon gate crossing the active region vertically at its center, with a width of 1 µm
# Gate centered at x = 5 µm, width = 1 µm, from x = 4.5 µm to x = 5.5 µm, y from 0 to 5 µm
gate = gdspy.Rectangle((4.5, 0), (5.5, 5), layer=2)
cell.add(gate)

# 3. Add two square contact holes, each 1 µm x 1 µm, positioned 1 µm away from the gate on either side along the active region
# Left contact hole positioned 1 µm left from gate edge, from x = 3.5 µm to x = 4.5 µm, y from 2 µm to 3 µm
left_contact = gdspy.Rectangle((3.5, 2), (4.5, 3), layer=3)
cell.add(left_contact)

# Right contact hole positioned 1 µm right from gate edge, from x = 5.5 µm to x = 6.5 µm, y from 2 µm to 3 µm
right_contact = gdspy.Rectangle((5.5, 2), (6.5, 3), layer=3)
cell.add(right_contact)

# Write the GDSII file
lib.write_gds('layout.gds')