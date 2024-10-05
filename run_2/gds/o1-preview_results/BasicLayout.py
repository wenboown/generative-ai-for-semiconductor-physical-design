import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell to contain the layout
cell = lib.new_cell('MYLAYOUT')

# Draw the rectangular active region with dimensions 10 µm x 5 µm on layer 1
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(active_region)

# Place a polysilicon gate that crosses the active region vertically at its center, with a width of 1 µm on layer 2
gate = gdspy.Rectangle((4.5, 0), (5.5, 5), layer=2)
cell.add(gate)

# Add two square contact holes, each 1 µm x 1 µm, positioned 1 µm away from the gate on either side along the active region on layer 3
# Left contact hole
left_contact = gdspy.Rectangle((2.5, 2), (3.5, 3), layer=3)
cell.add(left_contact)

# Right contact hole
right_contact = gdspy.Rectangle((6.5, 2), (7.5, 3), layer=3)
cell.add(right_contact)

# Save the design to a GDS file
lib.write_gds('layout.gds')